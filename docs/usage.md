# Usage Guide

This document provides guidance for both **end users** and **developers** who want to use or extend the credit card fraud detection system.

> See the [developer usage guide](usage_dev.md) for training, notebooks, and full environment setup.

---

## For Users (CLI Prediction Only)

You can use the prediction system from the command line to process a `.csv` file containing transactions.

### 1. Clone the repository

```
https://github.com/cfrBernard/ML-Fraud-Analysis.git
cd ML-Fraud-Analysis
```

### 2. Install dependencies

It is recommended to use a virtual environment.

```
pip install -e .
```

> requires-python = ">=3.11"

### 3. Run a prediction

Place your CSV input file inside the `data/` directory (e.g., `data/my_transactions.csv`), then run:

```
fraud-predict --file data/my_transactions.csv --threshold 0.30
```

- --file: Path to your CSV input.

- --threshold: Probability threshold to classify as fraud (default: 0.30).

> This will generate a predicted_output.csv with probabilities and predictions.

---

## CLI Output Example

Running the command will generate a summary like:

```
📊 Prediction Summary
────────────────────────────────────────────
📁 File processed         : data/to_predict.csv
🔢 Total transactions     : 100000
🚨 Predicted frauds       : 172
💾 Output saved to        : predicted_output.csv
```

> For full evaluation and metrics comparison, refer to the full [Results Documentation](results.md).

---

## 📎 Additional Notes
- 📂 Input CSV: The input file must be placed in the data/ folder (e.g. data/my_transactions.csv).
- 📄 Output: The prediction results will be saved to predicted_output.csv in the project root.
- ⚙️ Threshold configuration: You can adjust the classification threshold using the --threshold flag. Default is 0.3.

```
fraud-predict --file data/my_transactions.csv --threshold 0.4
```

> For contributors, see the [developer usage guide](usage_dev.md) for editable installs and advanced setup.
