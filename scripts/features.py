import pandas as pd

def amount_risk_flag(amount):
    """
    Flags transactions with amounts typically associated with higher fraud risk.
    Returns 1 if the amount is between 100 and 1000, else 0.
    """
    return 1 if 100 <= amount <= 1000 else 0

def compute_risk_features(row, risk_dict):
    """
    Computes risk-related features based on custom rules defined in the risk config.

    Returns:
        - risk_score : Total fraud risk score (weighted)
        - risk_low   : Count of low-risk triggers
        - risk_mid   : Count of mid-risk triggers
        - risk_high  : Count of high-risk triggers
    """
    score = 0
    risk_counts = {"low": 0, "mid": 0, "high": 0}

    for level, features in risk_dict.items():
        level_score = {"low": 1, "mid": 2, "high": 3}[level]
        for feature, bins in features.items():
            value = row.get(feature, None)
            if value is None:
                continue
            for b in bins:
                low, high = b["range"]
                if low <= value < high:
                    score += level_score
                    risk_counts[level] += 1
                    break

    return pd.Series({
        "risk_score": score,
        "risk_low": risk_counts["low"],
        "risk_mid": risk_counts["mid"],
        "risk_high": risk_counts["high"]
    })

def apply_threshold(proba, threshold):
    return (proba > threshold).astype(int)
