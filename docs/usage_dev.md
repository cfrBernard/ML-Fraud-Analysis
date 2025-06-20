# Developer usage guide

To contribute, test, or retrain the model, you will need the full development setup.

### 1. Clone the repository

```
https://github.com/cfrBernard/ML-Fraud-Analysis.git
cd ML-Fraud-Analysis
```

### 2. Editable install

It is recommended to use a virtual environment.

```
pip install -e .[dev] 
```

> requires-python = ">=3.11"

### 3. Project structure

```
├── assets/                     # Static files such as images or visual assets  
├── data/                       # Configuration or raw data  
├── docs/                       # Technical or user documentation  
├── models/                     # Trained models  
├── notebooks/                  
│   ├── 01_exploration.ipynb    # Exploratory data analysis  
│   └── 02_modeling.ipynb       # Model training and evaluation  
├── scripts/                     
│   ├── features.py             # Feature extraction and engineering  
│   └── predict.py              # Prediction script  
└── pyproject.toml              # Project configuration
```

### 4. Custom development

- Feature logic is in scripts/features.py
- Prediction logic is in scripts/predict.py
- Model training lives in notebooks/02_modeling.ipynb

---

## Dataset Setup

👉 [**Download the dataset here**](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

Once downloaded, place the creditcard.csv file inside the data/ directory

> This file is only needed for training and evaluation in notebooks — not for the CLI predictions.

---

## Run a prediction

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

## Additional Notes
- Input CSV: The input file must be placed in the data/ folder (e.g. data/my_transactions.csv).
- Output: The prediction results will be saved to predicted_output.csv in the project root.
- Threshold configuration: You can adjust the classification threshold using the --threshold flag. Default is 0.3.

```
fraud-predict --file data/my_transactions.csv --threshold 0.4
```
