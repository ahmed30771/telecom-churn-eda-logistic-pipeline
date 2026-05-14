# **Telcom Customer Churn Exploratory Data Analysis**
---
## **Sample Data:**
| customerID   | gender   |   SeniorCitizen | Partner   | Dependents   |   tenure | PhoneService   | MultipleLines   | InternetService   | OnlineSecurity   | OnlineBackup   | DeviceProtection   | TechSupport   | StreamingTV   | StreamingMovies   | Contract       | PaperlessBilling   | PaymentMethod             |   MonthlyCharges |   TotalCharges | Churn   |
|:-------------|:---------|----------------:|:----------|:-------------|---------:|:---------------|:----------------|:------------------|:-----------------|:---------------|:-------------------|:--------------|:--------------|:------------------|:---------------|:-------------------|:--------------------------|-----------------:|---------------:|:--------|
| 4086-ATNFV   | Female   |               0 | Yes       | Yes          |       34 | Yes            | No              | DSL               | Yes              | Yes            | Yes                | No            | No            | No                | One year       | Yes                | Mailed check              |            60.8  |        2042.05 | No      |
| 4248-QPAVC   | Female   |               1 | Yes       | No           |       17 | Yes            | Yes             | Fiber optic       | Yes              | No             | Yes                | No            | No            | No                | Month-to-month | Yes                | Bank transfer (automatic) |            85.35 |        1463.45 | Yes     |
| 3179-GBRWV   | Male     |               1 | Yes       | No           |       21 | Yes            | No              | DSL               | Yes              | Yes            | No                 | No            | No            | Yes               | Month-to-month | Yes                | Bank transfer (automatic) |            64.95 |        1339.8  | No      |
| 3370-GQEAL   | Male     |               0 | Yes       | Yes          |       30 | Yes            | Yes             | Fiber optic       | No               | No             | No                 | No            | Yes           | No                | Month-to-month | No                 | Electronic check          |            85.45 |        2509.95 | No      |
| 6865-JZNKO   | Female   |               0 | No        | No           |       30 | Yes            | No              | DSL               | Yes              | Yes            | No                 | No            | No            | No                | Month-to-month | Yes                | Bank transfer (automatic) |            55.3  |        1530.6  | No      |

---
---
## **Data Overview:**
```
Rows: 7043
Columns: 20
```

```
Duplicated Columns: 0 (0.0%)
Duplicated Rows: 22 (0.3%)
```
```
Total NaN Values: 11
Total NaN Rows: 11
Total NaN Rows Percentage: 0.16%
```
|                  |   total_nan | nan%   | dtypes   |   uniques | mean   | median   | mode             | std     | min   | 25%    | 50%     | 75%     | max    |
|:-----------------|------------:|:-------|:---------|----------:|:-------|:---------|:-----------------|:--------|:------|:-------|:--------|:--------|:-------|
| Churn            |           0 | 0.0%   | str      |         2 | -      | -        | No               | -       | -     | -      | -       | -       | -      |
| Contract         |           0 | 0.0%   | str      |         3 | -      | -        | Month-to-month   | -       | -     | -      | -       | -       | -      |
| Dependents       |           0 | 0.0%   | str      |         2 | -      | -        | No               | -       | -     | -      | -       | -       | -      |
| DeviceProtection |           0 | 0.0%   | str      |         3 | -      | -        | No               | -       | -     | -      | -       | -       | -      |
| InternetService  |           0 | 0.0%   | str      |         3 | -      | -        | Fiber optic      | -       | -     | -      | -       | -       | -      |
| MonthlyCharges   |           0 | 0.0%   | float64  |      1585 | 64.76  | 70.35    | 20.05            | 30.09   | 18.25 | 35.5   | 70.35   | 89.85   | 118.75 |
| MultipleLines    |           0 | 0.0%   | str      |         3 | -      | -        | No               | -       | -     | -      | -       | -       | -      |
| OnlineBackup     |           0 | 0.0%   | str      |         3 | -      | -        | No               | -       | -     | -      | -       | -       | -      |
| OnlineSecurity   |           0 | 0.0%   | str      |         3 | -      | -        | No               | -       | -     | -      | -       | -       | -      |
| PaperlessBilling |           0 | 0.0%   | str      |         2 | -      | -        | Yes              | -       | -     | -      | -       | -       | -      |
| Partner          |           0 | 0.0%   | str      |         2 | -      | -        | No               | -       | -     | -      | -       | -       | -      |
| PaymentMethod    |           0 | 0.0%   | str      |         4 | -      | -        | Electronic check | -       | -     | -      | -       | -       | -      |
| PhoneService     |           0 | 0.0%   | str      |         2 | -      | -        | Yes              | -       | -     | -      | -       | -       | -      |
| SeniorCitizen    |           0 | 0.0%   | int64    |         2 | 0.16   | 0.0      | 0                | 0.37    | 0.0   | 0.0    | 0.0     | 0.0     | 1.0    |
| StreamingMovies  |           0 | 0.0%   | str      |         3 | -      | -        | No               | -       | -     | -      | -       | -       | -      |
| StreamingTV      |           0 | 0.0%   | str      |         3 | -      | -        | No               | -       | -     | -      | -       | -       | -      |
| TechSupport      |           0 | 0.0%   | str      |         3 | -      | -        | No               | -       | -     | -      | -       | -       | -      |
| TotalCharges     |          11 | 0.16%  | float64  |      6530 | 2283.3 | 1397.475 | 20.2             | 2266.77 | 18.8  | 401.45 | 1397.48 | 3794.74 | 8684.8 |
| gender           |           0 | 0.0%   | str      |         2 | -      | -        | Male             | -       | -     | -      | -       | -       | -      |
| tenure           |           0 | 0.0%   | int64    |        73 | 32.37  | 29.0     | 1                | 24.56   | 0.0   | 9.0    | 29.0    | 55.0    | 72.0   |



---
---
## **Data Categories:**
| Data Category | Columns |
|---|---|
| **Numeric Data** | `tenure`, `TotalCharges`, `MonthlyCharges` |
| **Binary Numeric Data** | `SeniorCitizen` |
| **Binary Categorical Data** | `gender`, `Partner`, `Dependents`, `PhoneService`, `PaperlessBilling`, `Churn` |
| **Multiclass Ordinal Data** | `Contract` |
| **Multiclass Nominal Data** | `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `PaymentMethod` |
---
---
## **Data Distribution:**

### gender Data Distribution:

![gender Distribution Graph](images/gender_countplot.svg)

### SeniorCitizen Data Distribution:

![SeniorCitizen Distribution Graph](images/SeniorCitizen_countplot.svg)

### Partner Data Distribution:

![Partner Distribution Graph](images/Partner_countplot.svg)

### Dependents Data Distribution:

![Dependents Distribution Graph](images/Dependents_countplot.svg)

### PhoneService Data Distribution:

![PhoneService Distribution Graph](images/PhoneService_countplot.svg)

### MultipleLines Data Distribution:

![MultipleLines Distribution Graph](images/MultipleLines_countplot.svg)

### InternetService Data Distribution:

![InternetService Distribution Graph](images/InternetService_countplot.svg)

### OnlineSecurity Data Distribution:

![OnlineSecurity Distribution Graph](images/OnlineSecurity_countplot.svg)

### OnlineBackup Data Distribution:

![OnlineBackup Distribution Graph](images/OnlineBackup_countplot.svg)

### DeviceProtection Data Distribution:

![DeviceProtection Distribution Graph](images/DeviceProtection_countplot.svg)

### TechSupport Data Distribution:

![TechSupport Distribution Graph](images/TechSupport_countplot.svg)

### StreamingTV Data Distribution:

![StreamingTV Distribution Graph](images/StreamingTV_countplot.svg)

### StreamingMovies Data Distribution:

![StreamingMovies Distribution Graph](images/StreamingMovies_countplot.svg)

### Contract Data Distribution:

![Contract Distribution Graph](images/Contract_countplot.svg)

### PaperlessBilling Data Distribution:

![PaperlessBilling Distribution Graph](images/PaperlessBilling_countplot.svg)

### PaymentMethod Data Distribution:

![PaymentMethod Distribution Graph](images/PaymentMethod_countplot.svg)

### Churn Data Distribution:

![Churn Distribution Graph](images/Churn_countplot.svg)

---
---
## **Churn Data Imbalance:**
- Non-churn customers: 73.5%%

- Churn customers: 26.5%%

| Churn   |   count | pct_count   |
|:--------|--------:|:------------|
| No      |    5174 | 73.5%       |
| Yes     |    1869 | 26.5%       |

---
---
## **Outlier:**
Outliers on different thresholds.

|    | column         |   t_1 |   t_1.5 |   t_2 |   t_2.5 |   t_3 |   t_4 |
|---:|:---------------|------:|--------:|------:|--------:|------:|------:|
|  0 | tenure         |     0 |       0 |     0 |       0 |     0 |     0 |
|  1 | MonthlyCharges |     0 |       0 |     0 |       0 |     0 |     0 |
|  2 | TotalCharges   |   277 |       0 |     0 |       0 |     0 |     0 |

![BoxPlot](images/outliers_boxplot_tenure.svg)

![BoxPlot](images/outliers_boxplot_MonthlyCharges.svg)

![BoxPlot](images/outliers_boxplot_TotalCharges.svg)

---
---
## **Bivariate Analysis:**
### 1. Contract vs Churn:
- Month-to-month, high churn
- 2-year contract, low churn

![Contract vs Churn](images/contract_vs_churn.svg)

### 2. MonthlyCharges vs Churn:
- high bill, more churn
- Low charges, less churn

![MonthlyCharges vs Churn](images/monthlycharges_vs_churn.svg)

### 3. Tenure vs Churn:
- Low tenure, high churn
- High tenure, loyal customers

![Tenure vs Churn](images/tenure_vs_churn.svg)

---
---
## **Multivariate Analysis:**
### Contract, MonthlyCharges, Churn:


**Month-to-month Contract**

- High MonthlyCharges, more churn

- Low MonthlyCharges, comparatively less churn



**One year Contract**

- Moderate churn



**Two year Contract**

- Almost no churn (even if charges high)

![contract vs monthlycharges vs churn Histplot](images/hist_contract_monthlycharges_churn.svg)

---
---
## **Correlation Analysis:**
Highly correlated features. 0.7

|    | Feature1         | Feature2         |   Correlation |
|---:|:-----------------|:-----------------|--------------:|
|  0 | gender           | SeniorCitizen    |    nan        |
|  1 | gender           | Partner          |    nan        |
|  2 | gender           | Dependents       |    nan        |
|  3 | gender           | tenure           |    nan        |
|  4 | gender           | PhoneService     |    nan        |
|  5 | gender           | PaperlessBilling |    nan        |
|  6 | gender           | MonthlyCharges   |    nan        |
|  7 | gender           | TotalCharges     |    nan        |
|  8 | gender           | Churn            |    nan        |
|  9 | SeniorCitizen    | gender           |    nan        |
| 10 | SeniorCitizen    | Partner          |    nan        |
| 11 | SeniorCitizen    | Dependents       |    nan        |
| 12 | SeniorCitizen    | tenure           |    nan        |
| 13 | SeniorCitizen    | PhoneService     |    nan        |
| 14 | SeniorCitizen    | PaperlessBilling |    nan        |
| 15 | SeniorCitizen    | MonthlyCharges   |    nan        |
| 16 | SeniorCitizen    | TotalCharges     |    nan        |
| 17 | SeniorCitizen    | Churn            |    nan        |
| 18 | Partner          | gender           |    nan        |
| 19 | Partner          | SeniorCitizen    |    nan        |
| 20 | Partner          | Dependents       |    nan        |
| 21 | Partner          | tenure           |    nan        |
| 22 | Partner          | PhoneService     |    nan        |
| 23 | Partner          | PaperlessBilling |    nan        |
| 24 | Partner          | MonthlyCharges   |    nan        |
| 25 | Partner          | TotalCharges     |    nan        |
| 26 | Partner          | Churn            |    nan        |
| 27 | Dependents       | gender           |    nan        |
| 28 | Dependents       | SeniorCitizen    |    nan        |
| 29 | Dependents       | Partner          |    nan        |
| 30 | Dependents       | tenure           |    nan        |
| 31 | Dependents       | PhoneService     |    nan        |
| 32 | Dependents       | PaperlessBilling |    nan        |
| 33 | Dependents       | MonthlyCharges   |    nan        |
| 34 | Dependents       | TotalCharges     |    nan        |
| 35 | Dependents       | Churn            |    nan        |
| 36 | tenure           | gender           |    nan        |
| 37 | tenure           | SeniorCitizen    |    nan        |
| 38 | tenure           | Partner          |    nan        |
| 39 | tenure           | Dependents       |    nan        |
| 40 | tenure           | PhoneService     |    nan        |
| 41 | tenure           | PaperlessBilling |    nan        |
| 42 | tenure           | MonthlyCharges   |    nan        |
| 43 | tenure           | TotalCharges     |      0.825464 |
| 44 | tenure           | Churn            |    nan        |
| 45 | PhoneService     | gender           |    nan        |
| 46 | PhoneService     | SeniorCitizen    |    nan        |
| 47 | PhoneService     | Partner          |    nan        |
| 48 | PhoneService     | Dependents       |    nan        |
| 49 | PhoneService     | tenure           |    nan        |
| 50 | PhoneService     | PaperlessBilling |    nan        |
| 51 | PhoneService     | MonthlyCharges   |    nan        |
| 52 | PhoneService     | TotalCharges     |    nan        |
| 53 | PhoneService     | Churn            |    nan        |
| 54 | PaperlessBilling | gender           |    nan        |
| 55 | PaperlessBilling | SeniorCitizen    |    nan        |
| 56 | PaperlessBilling | Partner          |    nan        |
| 57 | PaperlessBilling | Dependents       |    nan        |
| 58 | PaperlessBilling | tenure           |    nan        |
| 59 | PaperlessBilling | PhoneService     |    nan        |
| 60 | PaperlessBilling | MonthlyCharges   |    nan        |
| 61 | PaperlessBilling | TotalCharges     |    nan        |
| 62 | PaperlessBilling | Churn            |    nan        |
| 63 | MonthlyCharges   | gender           |    nan        |
| 64 | MonthlyCharges   | SeniorCitizen    |    nan        |
| 65 | MonthlyCharges   | Partner          |    nan        |
| 66 | MonthlyCharges   | Dependents       |    nan        |
| 67 | MonthlyCharges   | tenure           |    nan        |
| 68 | MonthlyCharges   | PhoneService     |    nan        |
| 69 | MonthlyCharges   | PaperlessBilling |    nan        |
| 70 | MonthlyCharges   | TotalCharges     |    nan        |
| 71 | MonthlyCharges   | Churn            |    nan        |
| 72 | TotalCharges     | gender           |    nan        |
| 73 | TotalCharges     | SeniorCitizen    |    nan        |
| 74 | TotalCharges     | Partner          |    nan        |
| 75 | TotalCharges     | Dependents       |    nan        |
| 76 | TotalCharges     | tenure           |      0.825464 |
| 77 | TotalCharges     | PhoneService     |    nan        |
| 78 | TotalCharges     | PaperlessBilling |    nan        |
| 79 | TotalCharges     | MonthlyCharges   |    nan        |
| 80 | TotalCharges     | Churn            |    nan        |
| 81 | Churn            | gender           |    nan        |
| 82 | Churn            | SeniorCitizen    |    nan        |
| 83 | Churn            | Partner          |    nan        |
| 84 | Churn            | Dependents       |    nan        |
| 85 | Churn            | tenure           |    nan        |
| 86 | Churn            | PhoneService     |    nan        |
| 87 | Churn            | PaperlessBilling |    nan        |
| 88 | Churn            | MonthlyCharges   |    nan        |
| 89 | Churn            | TotalCharges     |    nan        |

![Correlation](images/correlations.svg)


---
---
## **Key Business Insights:**

- Month-to-month contracts have highest churn

- Low tenure customers are most likely to churn

- High monthly charges increase churn risk


