"""
UFGS Utils Module
- Parses UFGS .SEC files
- Extracts structured headings, metadata, and submittals
- Supports keyword warnings, discipline tagging, and structured export
"""

import os
import re
import pandas as pd
from lxml import etree

# Dynamic debug toggle
DEBUG_MODE = False

def debug_print(msg):
    if DEBUG_MODE:
        print(f"[DEBUG] {msg}")

def clean_text(text):
    return re.sub(r'[^ -~]+', '', text.strip()) if text else ''

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
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            raw = re.sub(r'[^\x09\x0A\x0D\x20-\x7E]', '', f.read())
        root = etree.fromstring(raw.encode('utf-8'))
    except Exception as e:
        debug_print(f"Failed to parse {path}: {e}")
        return []

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

def tag_label(row):
    tag = row['SEC TAG']
    num = row['Number']
    depth = row['NEST_DEPTH']
    if depth == 0:
        return 'Heading'
    if tag == '<PRT>':
        return 'PART'
    if tag == '<SPT>':
        if num.count('.') == 1:
            return 'ARTICLE'
        elif num.count('.') == 2:
            return 'Paragraph'
        else:
            return 'Subparagraph'
    if tag == '<ENG>':
        return 'English Measurement Units'
    if tag == '<MET>':
        return 'Metric Measurement Units'
    if tag == '<PRA>':
        return 'Preparing Activity'
    if tag == '<SCP>':
        return 'Section Scope'
    return ''

