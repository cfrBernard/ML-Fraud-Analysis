import pandas as pd
import argparse
import pickle
import json
import numpy as np
import os
from scripts.features import amount_risk_flag, compute_risk_features, apply_threshold

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default="data/to_predict.csv", help="CSV input file")
    parser.add_argument("--threshold", type=float, default=0.3, help="Fraud threshold")
    args = parser.parse_args()

    # Relative paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(BASE_DIR, "models", "model.pkl")
    config_path = os.path.join(BASE_DIR, "data", "risk_config.json")
    input_path = os.path.join(BASE_DIR, args.file)
    output_path = os.path.join(BASE_DIR, "predicted_output.csv")

    # Load model
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Load risk config
    with open(config_path, "r") as f:
        risk_dict = json.load(f)

    # Convert ranges
    for level in risk_dict:
        for feature in risk_dict[level]:
            for b in risk_dict[level][feature]:
                b["range"] = tuple(b["range"])

    # Load data
    df = pd.read_csv(input_path)

    # Generate features
    risk_features = df.apply(compute_risk_features, axis=1, risk_dict=risk_dict)
    df['amount_high_fraud_zone'] = df['Amount'].apply(amount_risk_flag)
    df = pd.concat([df.drop(columns=risk_features.columns, errors='ignore'), risk_features], axis=1)

    features = ['V4', 'V10', 'V11', 'V12', 'V14', 'V17', 'Amount', 
                'risk_score', 'risk_low', 'risk_mid', 'risk_high', 
                'amount_high_fraud_zone']
    X = df[features]

    # Predict
    y_proba = model.predict_proba(X)[:, 1]
    df['fraud_proba'] = y_proba
    df['fraud_predicted'] = apply_threshold(y_proba, args.threshold)

    # Save results
    df.to_csv(output_path, index=False)

    # Console summary
    total = len(df)
    predicted_frauds = int(df['fraud_predicted'].sum())

    print("\n📊 Prediction Summary")
    print("────────────────────────────────────────────")
    print(f"📁 File processed         : {args.file}")
    print(f"🔢 Total transactions     : {total}")
    print(f"🚨 Predicted frauds       : {predicted_frauds}")
    print(f"💾 Output saved to        : predicted_output.csv\n")

if __name__ == "__main__":
    main()