#!/usr/bin/env python3
"""
Optional extractor for DOS edition text.

Usage:
  1) Dump your own legally obtained game directory to ./_dos_dump
  2) Run: python scripts/ingest_dos_assets.py
  3) It will attempt to parse text assets and write JSON under data/world and data/cases.

NOTE: Original DOS formats vary; you'll likely need to add custom parsers.
This script includes stubs and guidance (strings search, code pages, etc.).
"""
from pathlib import Path

DUMP = Path("_dos_dump")
OUT = Path("data") / "world"

def main():
    if not DUMP.exists():
        print("Place your DOS dump at ./_dos_dump and rerun.")
        return
    # TODO: implement parsing of text/clue files from DOS resources.
    # Hints:
    # - Search for readable strings (latin-1/CP437): e.g., file.read().decode('cp437', errors='ignore')
    # - Build a simple state machine to group clue paragraphs by location.
    # - Normalize whitespace and write to JSON schema seen in data/world/locations.json
    print("Stub only — add parsers for your dump format.")

if __name__ == "__main__":
    main()
