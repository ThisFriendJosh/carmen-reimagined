import json, pathlib

def test_locations_json_valid():
    p = pathlib.Path(__file__).resolve().parents[1] / 'data' / 'world' / 'locations.json'
    obj = json.loads(p.read_text())
    assert 'locations' in obj
    for k, v in obj['locations'].items():
        assert all(key in v for key in ('id','name','country','lat','lon','neighbors','clues'))
