"""Pure deterministic scoring and peer-comparison functions."""
from __future__ import annotations
from typing import Dict, Iterable, List


def absolute_score(criteria: Iterable[dict]) -> float:
    """Sum (score / max_score) * weight. Keep full precision internally."""
    total = 0.0
    for item in criteria:
        maximum = float(item["max_score"])
        if maximum <= 0:
            raise ValueError("max_score must be positive")
        total += float(item["score"]) / maximum * float(item["weight"])
    return total


def add_peer_metrics(suppliers: List[dict]) -> List[dict]:
    """Mutate score rows with benchmark, gap, relative_percent, and PPI."""
    criterion_ids = sorted({c["criterion_id"] for s in suppliers for c in s["criteria"]})
    benchmarks: Dict[int, float] = {}
    for cid in criterion_ids:
        benchmarks[cid] = max(
            (float(c["score"]) for s in suppliers for c in s["criteria"] if c["criterion_id"] == cid),
            default=0.0,
        )
    for supplier in suppliers:
        weighted_relative = 0.0
        total_weight = 0.0
        for item in supplier["criteria"]:
            benchmark = benchmarks[item["criterion_id"]]
            score = float(item["score"])
            weight = float(item["weight"])
            relative = 100.0 if benchmark == 0 else score / benchmark * 100.0
            item.update(benchmark=benchmark, gap=score-benchmark, relative_percent=relative,
                        absolute_contribution=score/float(item["max_score"])*weight,
                        ppi_contribution=relative*weight/100.0)
            weighted_relative += relative * weight
            total_weight += weight
        supplier["absolute_score"] = absolute_score(supplier["criteria"])
        supplier["ppi"] = weighted_relative / total_weight if total_weight else 0.0
    return suppliers
