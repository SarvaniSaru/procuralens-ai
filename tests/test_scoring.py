from src.scoring import absolute_score, add_peer_metrics

def test_absolute_score():
    assert absolute_score([{"score":8,"max_score":10,"weight":30},{"score":5,"max_score":10,"weight":20}]) == 34

def test_zero_benchmark():
    rows=[{"criteria":[{"criterion_id":1,"score":0,"max_score":10,"weight":100}]}]
    assert add_peer_metrics(rows)[0]["criteria"][0]["relative_percent"] == 100
