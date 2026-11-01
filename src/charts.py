def normalized_percent(score, maximum):
    return 0.0 if maximum == 0 else float(score) / float(maximum) * 100.0
