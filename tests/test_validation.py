from src.validation import parse_json_object, normalize_criteria, zero_fallback

def test_fenced_json(): assert parse_json_object('```json\n{"x":1}\n```')["x"] == 1

def test_missing_and_clipping():
    criteria=[{"criterion_id":1,"max_score":10},{"criterion_id":2,"max_score":5}]
    out,w=normalize_criteria({"criteria":[{"criterion_id":1,"proposed_score":12}]},criteria)
    assert out[0]["proposed_score"] == 10 and out[1]["proposed_score"] == 0 and w
