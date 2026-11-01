from src.ranking import rank_suppliers

def test_tie_break_order_and_exclusion():
    rows=[{"supplier_name":"B","ppi":90,"submission_date":"2026-01-02","experience_rating":8},{"supplier_name":"A","ppi":90,"submission_date":"2026-01-01","experience_rating":7},{"supplier_name":"X","ppi":100,"submission_date":"2026-01-01","experience_rating":10,"confirmed_non_compliant":True}]
    ranked=rank_suppliers(rows)
    assert [r["supplier_name"] for r in ranked] == ["A","B"]
    assert [r["final_rank"] for r in ranked] == [1,2]
