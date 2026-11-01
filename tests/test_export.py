from pathlib import Path
import json

def test_sample_export():
    p=Path(__file__).parents[1]/"sample_output"/"sample_run.json"
    data=json.loads(p.read_text())
    assert data["rfp_run_id"] and len(data["suppliers"]) >= 4
