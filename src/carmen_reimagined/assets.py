from dataclasses import dataclass
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]

@dataclass
class Theme:
    bg_color: tuple = (18, 18, 20)
    fg_color: tuple = (235, 235, 235)
    accent: tuple = (255, 204, 0)

def asset_path(*parts) -> Path:
    return BASE / "assets" / Path(*parts)
