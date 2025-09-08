from dataclasses import dataclass
from typing import List, Dict, Optional
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]

@dataclass
class Location:
    id: str
    name: str
    country: str
    lat: float
    lon: float
    neighbors: list
    clues: list

@dataclass
class World:
    locations: Dict[str, Location]

    @classmethod
    def load(cls, path: Path) -> "World":
        obj = json.loads(path.read_text())
        locs = {k: Location(**v) for k, v in obj["locations"].items()}
        return cls(locs)

def load_world() -> World:
    return World.load(BASE / "data" / "world" / "locations.json")
