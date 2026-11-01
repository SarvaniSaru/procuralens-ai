"""Required deterministic ranking rules."""
from __future__ import annotations
from typing import List


def rank_suppliers(suppliers: List[dict]) -> List[dict]:
    eligible = [dict(s) for s in suppliers if not s.get("confirmed_non_compliant", False)]
    eligible.sort(key=lambda s: (
        -float(s["ppi"]),
        str(s["submission_date"]),
        -float(s["experience_rating"]),
        str(s["supplier_name"]).casefold(),
        str(s["supplier_name"]),
    ))
    for rank, supplier in enumerate(eligible, 1):
        supplier["final_rank"] = rank
    return eligible
