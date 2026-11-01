def approved_feedback(rows):
    """Return only feedback approved for reuse as future prompt guidance."""
    return [r for r in rows if r.get("approved")]
