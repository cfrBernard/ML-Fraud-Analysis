# Credit Card Fraud Detection

This project focuses on detecting fraudulent transactions from a highly imbalanced credit card dataset using exploratory data analysis and zone-based feature engineering.

The goal is to better understand the structure of fraudulent activity by **identifying high-, medium-, and low-risk zones** in the feature space — paving the way for interpretable rules and better model input features.

[**Download the dataset here**](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

![Version](https://img.shields.io/badge/version-v0.1.0-blue)
![License](https://img.shields.io/github/license/cfrBernard/ML-Fraud-Analysis)

---

<br>

<p align="center">
  <img src="assets/img/illustration credit card fraud detection.png" alt="dataAnalysis illu" />
</p>

---

## Project Overview
Credit card fraud detection is a critical problem complicated by the extreme imbalance between legitimate and fraudulent transactions. This project explores:

- Data visualization and statistical analysis of transaction features
- Defining fraud risk zones based on feature distributions
- Engineering risk-score features to improve detection
- Building interpretable and effective machine learning models
> The approach enables both ML-driven and rule-based fraud detection workflows.

## Objectives
- Extract interpretable, risk-based features to augment fraud detection models
- Provide a flexible framework for hybrid detection systems combining ML and rules
- Achieve high recall on fraudulent transactions while controlling false positives

## Key Features
- Zone-based risk scoring on continuous features
- Threshold-based fraud classification with adjustable sensitivity
- CLI tool for batch prediction on new data files
- Modular code structure for easy extension and maintenance
 
---

## Results

// NEED OVERVIEW

For an in-depth analysis with detailed evaluation reports and visualizations, please refer to the full [Results Documentation](docs/results.md).

---

## Project Structure

```
assets/          # Images and visual assets
data/            # Input data and configuration files
models/          # Serialized ML models
notebooks/       # Exploratory and modeling notebooks
scripts/         # Source code: features extraction, prediction CLI
docs/            # Detailed documentation and results (to be added)
```

## How to Use

This project supports both end users and developers:

- **End users** can easily run predictions on their data with the provided CLI tool.
- **Developers** can explore the codebase, customize feature engineering, and retrain models.

> For step-by-step instructions, installation guidelines, and developer notes (including dependency management and environment setup), see the dedicated [Usage Guide](docs/usage.md).

---

## Contact
For issues, suggestions, or contributions, feel free to open an issue on the GitHub repository.

> This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for details.
