# Telecom Customer Churn Prediction (EDA + ML Pipeline)

End-to-end Machine Learning project for predicting telecom customer churn using detailed Exploratory Data Analysis (EDA), data preprocessing, and a fully automated Logistic Regression pipeline with hyperparameter tuning.

---

## Project Objective

Telecom companies lose revenue when customers leave their service (churn).  
This project aims to predict whether a customer will churn or not based on usage patterns, contract type, billing, and service features.

---

## Dataset Information

- Source: Telecom Customer Churn Dataset
- Rows: 7043
- Columns: 20
- Target Variable: `Churn` (Yes / No)

---

## Problem Statement

Given customer demographic and service-related features, predict whether a customer will churn in the future to help the business take preventive actions.

---

## Exploratory Data Analysis (EDA)

EDA was performed to understand data distribution, patterns, and business insights.

### Key Steps:
- Data overview (shape, types, missing values, duplicates)
- Feature categorization (numeric, ordinal, nominal, binary)
- Distribution analysis using countplots
- Outlier detection using IQR method
- Bivariate analysis (feature vs churn)
- Multivariate analysis
- Correlation analysis

### Key Insights:
- Month-to-month contracts have highest churn rate
- Customers with low tenure are more likely to churn
- Higher monthly charges increase churn probability
- Long-term contracts significantly reduce churn risk

---

## Data Preprocessing

Custom preprocessing pipeline implemented in `src/preprocessing.py`:

### Steps:
- Remove duplicate rows
- Handle missing values
- Convert incorrect data types
- Replace empty strings with NaN
- Outlier handling using IQR clipping

---

## Machine Learning Pipeline

A fully automated ML pipeline was built using Scikit-learn.

### Model Used:
- Logistic Regression

---

## Pipeline Components

### 1. Target Encoding
- Label Encoding applied to `Churn`

### 2. Train-Test Split
- Stratified split to maintain class distribution

### 3. ColumnTransformer
- Numeric Features:
  - SimpleImputer (median)
  - StandardScaler

- Nominal Features:
  - SimpleImputer (most frequent)
  - OneHotEncoder

- Ordinal Features:
  - SimpleImputer
  - OrdinalEncoder

- Remaining Features:
  - SimpleImputer only

---

## Hyperparameter Tuning

GridSearchCV used for optimization:

### Tuned Parameters:
- `C`: Regularization strength
- `solver`: Optimization algorithm
- `max_iter`: Iterations

### Validation:
- 5-Fold Cross Validation

---

## Model Evaluation

### Metrics:
- Accuracy Score (Train & Test)
- Best CV Score
- Best Hyperparameters
- Cross-validation results saved in CSV

---

## Model Saving

Best trained model is saved using Pickle:

---

## Project Structure
```markdown
- config/
    - config.yaml
- data/
    - telco_customer_churn.csv
- model/
    - churn_model.pkl
- notebook/
    - EDA.ipynb
    - EDA.md
    - images/...
- reports/
    - cv_report.csv
- src/
    - load_data.py
    - preprocessing.py
    - model_pipe.py
- .gitignore
- main.py
- README.md
- requirements.txt
```


## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Pipeline & ColumnTransformer
- GridSearchCV

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the full pipeline
python main.py
```  

---
## Future Improvements
- Try advanced models (Random Forest, XGBoost, LightGBM)
- Handle class imbalance (SMOTE / class_weight)
- Feature selection techniques
- Deploy using Streamlit or Flask
- Add SHAP for model explainability


---
## Author
**Muhammad Ahmed**  
*Aspiring Data Scientist | ML & AI Enthusiast*
