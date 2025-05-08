import os
import re
import zipfile
import requests
import pandas as pd
from lxml import etree

# --- Global Debug Toggle ---
DEBUG_MODE = False

def debug_print(msg):
    if DEBUG_MODE:
        print(msg)

# --- Discipline Map Loader ---
def load_discipline_map(csv_path):
    try:
        df = pd.read_csv(csv_path, comment='#')
        df.columns = [c.strip() for c in df.columns]
        if 'UFGS' not in df.columns or 'Discipline' not in df.columns:
            raise ValueError("Discipline CSV must contain 'UFGS' and 'Discipline' columns.")
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load discipline map from {csv_path}: {e}")

# --- Download UFGS ZIP File ---
def download_ufgs_zip(url, zip_path, force=False):
    if os.path.exists(zip_path) and not force:
        debug_print(f"Using existing zip at {zip_path}")
        return
    debug_print(f"Downloading zip from {url} to {zip_path}...")
    response = requests.get(url)
    response.raise_for_status()
    with open(zip_path, 'wb') as f:
        f.write(response.content)
    debug_print("Download complete.")

# --- Extract ZIP ---
def extract_zip(zip_path, extract_to):
    if os.path.exists(extract_to):
        debug_print(f"Removing existing extraction dir: {extract_to}")
        import shutil
        shutil.rmtree(extract_to)
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    debug_print("Extraction complete.")

# --- XML Helpers ---
def clean_text(text):
    return re.sub(r'[^\x20-\x7E]+', '', text.strip()) if text else ''

def extract_text(el):
    return clean_text(''.join(el.itertext())) if el is not None else ''

def get_line_number(el):
    return el.sourceline if hasattr(el, 'sourceline') else -1

def parse_children(el, depth, num_str, ufgs_id):
    rows = []
    for ch in el:
        if ch.tag in ['ENG', 'MET']:
            rows.append((depth+1, ch.tag, num_str, extract_text(ch), get_line_number(ch), None, None, ufgs_id))
        elif len(ch):
            rows += parse_children(ch, depth+1, num_str, ufgs_id)
    return rows

def parse_spt(el, depth, numbering, ufgs_id, submittal=None):
    rows = []
    num_str = '.'.join(map(str, numbering))
    rows.append((depth, 'SPT', num_str, extract_text(el.find('TTL')), get_line_number(el.find('TTL')), None, None, ufgs_id))
    for ch in el:
        tag = ch.tag
        if tag == 'SCP':
            rows.append((depth+1, 'SCP', num_str, extract_text(ch), get_line_number(ch), None, None, ufgs_id))
        elif tag == 'NTE':
            for npr in ch.findall('./NPR'):
                rows.append((depth+1, 'NPR', num_str, extract_text(npr), get_line_number(npr), None, None, ufgs_id))
        elif tag == 'TXT':
            rows.append((depth+1, 'TXT', num_str, extract_text(ch), get_line_number(ch), None, None, ufgs_id))
            rows += parse_children(ch, depth+1, num_str, ufgs_id)
        elif tag == 'LST':
            sub = ch.find('SUB')
            val = extract_text(sub)
            match = re.match(r"(SD-[0-9]{2})", val)
            submittal = match.group(1) if match else None
            rows.append((depth+1, 'LST', num_str, val, get_line_number(ch), submittal, None, ufgs_id))
        elif tag == 'ITM':
            subs = ch.findall('.//SUB')
            tag = 'SUB' if submittal else 'ITM'
            name = extract_text(subs[0]) if subs else extract_text(ch)
            clss = extract_text(subs[1]) if len(subs) > 1 else ''
            itm_depth = depth + 2 if submittal else depth + 1
            rows.append((itm_depth, tag, num_str, name, get_line_number(ch), submittal, clss, ufgs_id))
        elif tag == 'SPT':
            new_num = numbering + [len(el.findall('./SPT')) + 1]
            rows += parse_spt(ch, depth+1, new_num, ufgs_id, submittal)
    return rows

def parse_sec_file(path, ufgs_id):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        raw = f.read()
    raw = re.sub(r'[^\x09\x0A\x0D\x20-\x7E]', '', raw)
    root = etree.fromstring(raw.encode('utf-8'))
    rows = []
    for tag in ['SCN', 'STL', 'DTE', 'PRA']:
        for el in root.findall(f".//{tag}"):
            rows.append((0, tag, 'Heading', extract_text(el), get_line_number(el), None, None, ufgs_id))
    for p_idx, prt in enumerate(root.findall('.//PRT'), 1):
        ttl = extract_text(prt.find('TTL'))
        rows.append((1, 'PRT', str(p_idx), ttl, get_line_number(prt.find('TTL')), None, None, ufgs_id))
        for s_idx, spt in enumerate(prt.findall('./SPT'), 1):
            rows += parse_spt(spt, 2, [p_idx, s_idx], ufgs_id)
    return rows

# --- Batch Parser ---
def parse_all_sec_files(sec_dir, discipline_df):
    combined_rows = []
    missing_files = []
    ufgs_sections = {f"{row['UFGS']}.SEC": row['UFGS'] for _, row in discipline_df.iterrows()}
    for filename, ufgs_id in ufgs_sections.items():
        file_path = os.path.join(sec_dir, filename)
        if os.path.exists(file_path):
            debug_print(f"Parsing: {filename}")
            combined_rows += parse_sec_file(file_path, ufgs_id)
        else:
            missing_files.append(filename)
    return combined_rows, missing_files
