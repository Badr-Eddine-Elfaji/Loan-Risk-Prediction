# Loan Risk Prediction

## Description

This project focuses on predicting customer credit risk for loan approval using financial indicators and profile attributes. The model classifies customers into two categories: **0 (High Risk)** and **1 (Low Risk)**.
<img width="959" height="439" alt="image" src="https://github.com/user-attachments/assets/4ff955ad-5ad1-4394-a4ca-eac6149f40e0" />


## Key Features

* **Outlier Management:** Implements **Winsorization** (IQR-based clipping) and **Robust Scaling** to handle extreme values in financial data (Features A1-A4).
* **Tree-Based Modeling:** Utilizes **Random Forest** to capture non-linear relationships and maintain high accuracy despite skewed distributions.
* **Robust Preprocessing:** Scaled and transformed features to ensure stable model performance.

## Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn

## Project Structure

* `app.py`: The Streamlit web application for interactive model testing.
* `loan_risk_analysis.ipynb`: Main notebook for EDA, outlier handling, and model training.
* `gb_model.pkl`: The saved model file, exported via pickle.
* `Risque_data.xlsx`: The raw financial dataset. (in black box format)
* `requirements.txt`: List of dependencies.
* `README.md`: Documentation and instructions.
* `LICENSE`: The MIT license for this project.
* `.gitignore`: Configuration to keep the repository clean of temporary files.

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/Badr-Eddine-Elfaji/Loan-Risk-Prediction.git

```


2. Install dependencies:
```bash
pip install -r requirements.txt

```


3. Run the streamlit webapp using terminal (in the same folder):
```bash
streamlit run app.py

```


