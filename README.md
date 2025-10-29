# bracbank_vs_dsex
Analysis of BRACBANK stock returns vs DSEX index, including daily returns, volatility, and beta/alpha estimation using Python.

# BRACBANK vs DSEX Analysis

This project analyzes **BRACBANK stock returns** relative to the **DSEX index** using Python.  
It calculates **daily returns**, provides **descriptive statistics**, and performs a **linear regression** to estimate **beta** and **alpha**.

---

## Features

- **Daily Returns Calculation:**  
  BracBank returns are computed based on the previous close (YCP).  
  DSEX returns are calculated using percentage change.

- **Descriptive Statistics:**  
  - Mean, standard deviation, min, max, percentiles  
  - Correlation between BRACBANK and DSEX returns  

- **Linear Regression:**  
  - **Beta (slope):** measures stock sensitivity to the market  
  - **Alpha (intercept):** measures stock outperformance relative to the market  

- **Clean, PyCharm-ready code** for easy execution and replication

---

## Dependencies

- Python 3.8+
- pandas
- numpy
- scikit-learn

Install dependencies via:

```bash
pip install pandas numpy scikit-learn

