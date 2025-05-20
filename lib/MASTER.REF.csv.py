#!/usr/bin/env python3
"""
make_rid_rtl_table.py  (RID, Title, Organization order)
-------------------------------------------------------
Create a CSV (RID | Title | Organization) from MASTER.REF.XML.
"""

import argparse
import csv
from pathlib import Path
from typing import List, Dict
from lxml import etree as ET


def parse_xml(xml_path: Path, drop_brk: bool = True) -> List[Dict[str, str]]:
    parser = ET.XMLParser(recover=True, remove_blank_text=True)
    tree = ET.parse(str(xml_path), parser)
    root = tree.getroot()

    if drop_brk:
        for brk in root.findall(".//BRK"):
            parent = brk.getparent()
            if parent is not None:
                parent.remove(brk)

    rows = []
    for ref in root.findall(".//REF"):
        org_elem = ref.find("ORG")
        org_name = "".join(org_elem.itertext()).strip() if org_elem is not None else ""
        for rid_elem in ref.findall("RID"):
            rid = (rid_elem.text or "").strip()
            rtl_elem = rid_elem.getnext()
            while rtl_elem is not None and rtl_elem.tag != "RTL":
                rtl_elem = rtl_elem.getnext()
            if rtl_elem is None:
                continue
            title = "".join(rtl_elem.itertext()).strip()
            rows.append({"RID": rid, "Title": title, "Organization": org_name})
    return rows


def write_csv(rows: List[Dict[str, str]], csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["RID", "Title", "Organization"])
        writer.writeheader()
        writer.writerows(rows)


def main():
    ap = argparse.ArgumentParser(description="Create RID-RTL table (ordered columns)")
    ap.add_argument("--in", required=True, help="input MASTER.REF.XML")
    ap.add_argument("--csv_out", required=True, help="output CSV")
    ap.add_argument("--keep-brk", action="store_true", help="retain <BRK/> elements")
    args = ap.parse_args()

    rows = parse_xml(Path(args.in), drop_brk=not args.keep_brk)
    write_csv(rows, Path(args.csv_out))
    print(f"✔ Wrote {len(rows):,} rows → {args.csv_out}")


if __name__ == "__main__":
    main()
