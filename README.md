# Carmen Sandiego Reimagined (Modern Fork)

**Educational reimplementation** inspired by the classic DOS game. This repo contains _original code and data only_; 
you must supply any copyrighted game data yourself (see `scripts/ingest_dos_assets.py`).

## Goals
- Clean, testable architecture (Python + Pygame).
- Data-driven cases (JSON) and world graph (countries, cities, clues).
- Pluggable UI (swap Pygame with web later).
- Deterministic logic for reproducible gameplay (good for tests/AI agents).

## Quick Start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

## Project Layout
```
src/carmen_reimagined/
  game.py          # Game loop & router
  states.py        # State machine (Menu, CaseBrief, Travel, Interrogate, Warrant, Capture, Credits)
  data.py          # Data models & loaders (pydantic-lite)
  assets.py        # Asset loader/paths and theme
data/
  world/locations.json    # Countries/cities and connections
  cases/example_case.json # Sample case definition
assets/
  ui/placeholder.png
scripts/
  ingest_dos_assets.py    # Optional: parse text from DOS files (BYO game dump)
tests/
  test_data_schema.py
run.py
```

## Legal
This is a **from-scratch** educational work. Do not commit proprietary assets or ROMs. Name & references used under nominative fair use.
