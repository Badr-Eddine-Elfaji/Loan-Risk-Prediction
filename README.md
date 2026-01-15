# Loan Risk Prediction

## Description

This project focuses on predicting customer credit risk for loan approval using financial indicators and profile attributes. The model classifies customers into two categories: **0 (High Risk)** and **1 (Low Risk)**.

## Key Features

* **Outlier Management:** Implements **Winsorization** (IQR-based clipping) and **Robust Scaling** to handle extreme values in financial data (Features A1-A4).
* **Tree-Based Modeling:** Utilizes **Random Forest** to capture non-linear relationships and maintain high accuracy despite skewed distributions.
* **Robust Preprocessing:** Scaled and transformed features to ensure stable model performance.

## Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn

## Project Structure

* `data/`: Contains the dataset (if applicable).
* `notebooks/`: Jupyter notebooks with EDA and model training.
* `scripts/`: Python scripts for data preprocessing and prediction.

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/Badr-Eddine-Elfaji/Loan-Risk-Prediction.git

```


2. Install dependencies:
```bash
pip install -r requirements.txt

```


3. Run the analysis:
```bash
jupyter notebook notebooks/risk_analysis.ipynb

```


