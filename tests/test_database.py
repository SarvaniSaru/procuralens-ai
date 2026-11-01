from pathlib import Path

def test_seeded_database_exists():
    assert (Path(__file__).parents[1]/"data"/"procuralens.db").exists()
