"""Normalize untrusted LLM criterion results."""
from __future__ import annotations
import json, math, re


def parse_json_object(text: str) -> dict:
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.I|re.S)
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError("No JSON object found")
    return json.loads(text[start:end+1])


def zero_fallback(criteria: list[dict], rules: list[dict], warning: str) -> dict:
    return {
        "criteria": [{"criterion_id": c["criterion_id"], "proposed_score": 0,
                      "max_score": c["max_score"], "concise_justification": "Human review required.",
                      "references": [], "requires_review": True, "warnings": [warning]} for c in criteria],
        "knockout_rules": [{"rule_id": r["rule_id"], "result": "NOT FOUND",
                            "reasoning": "Human review required.", "references": []} for r in rules],
    }


def normalize_criteria(raw: dict, criteria: list[dict]) -> tuple[list[dict], list[str]]:
    warnings, seen = [], {}
    for item in raw.get("criteria", []) if isinstance(raw.get("criteria"), list) else []:
        try: cid = int(item.get("criterion_id"))
        except Exception: warnings.append("Invalid criterion ID removed"); continue
        if cid in seen: warnings.append(f"Duplicate criterion {cid} removed"); continue
        seen[cid] = item
    output = []
    for criterion in criteria:
        cid = criterion["criterion_id"]
        item = seen.get(cid, {})
        if not item: warnings.append(f"Missing criterion {cid} inserted with score zero")
        try: score = float(item.get("proposed_score", 0))
        except Exception: score = 0; warnings.append(f"Criterion {cid} score replaced with zero")
        if not math.isfinite(score): score = 0; warnings.append(f"Criterion {cid} non-finite score replaced")
        maximum = float(criterion["max_score"])
        clipped = max(0.0, min(maximum, score))
        if clipped != score: warnings.append(f"Criterion {cid} clipped from {score} to {clipped}")
        output.append({**item, "criterion_id": cid, "proposed_score": clipped, "max_score": maximum})
    return output, warnings
