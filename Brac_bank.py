import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


Index = pd.read_csv("index.csv").set_index('Date', drop=True)
Index["Index_return"] = Index["DSEX"].pct_change(-1)
Index.reset_index(inplace=True)                        # Resetting the index
Index.rename(columns= {'Date': 'DATE'}, inplace=True)  # Renaming the column to math with other dataframes

B_stock = pd.read_csv("BracBank.csv")
B_stock= B_stock.set_index('DATE', drop=True)
B_stock.reset_index(inplace=True)
B_stock["BracBank_return"] = (B_stock["CLOSEP"] - B_stock["YCP"]) / B_stock["YCP"]

B_stock['DATE'] = B_stock['DATE'].str.strip()
Index['DATE'] = Index['DATE'].str.strip() # Removing extra spaces.

Index['DATE'] = pd.to_datetime(Index['DATE'], format="%d-%m-%Y")
B_stock['DATE'] = pd.to_datetime(B_stock['DATE'], format="%d-%m-%y")

df = pd.merge(
    Index[['DATE', 'Index_return']],
    B_stock[['DATE', 'BracBank_return']],
    on='DATE',
    how='inner'
)
df.dropna(inplace=True) # Dropping the missing / Na values

print(df[['Index_return', 'BracBank_return']].describe())

# ------------------------------------------------------------------
# Analysis Summary based on 418 trading days
# ------------------------------------------------------------------

# Average Daily Returns
# Based on our 418 trading days data points:
# - The average daily return of the market is slightly negative: -0.03%
# - The average daily return of the stock is small positive: 0.179%
# We can state that the stock performed better in terms of market.

# Volatility (Standard Deviation)
# - Market volatility is around 0.9%
# - The stock moves roughly twice as much as the market on average, indicating higher beta.

# Range of Daily Returns
# - Daily return of the index ranged from -3% to +5.4%
# - Daily return of the stock ranged from -9.8% to +9.8%
# - The stock remains consistent with larger swings and higher volatility.

# Percentiles of Daily Returns (418 trading days)
# - 25th percentile: market -0.005819, stock -0.008000
# - 50th percentile: market -0.000678, stock 0.000000
# - 75th percentile: market 0.003817, stock 0.009507

Dataset= df[['Index_return', 'BracBank_return']]
Dataset.corr()

x = np.array(Dataset['Index_return']).reshape(-1, 1).astype(float)   # 2D array
y = np.array(Dataset['BracBank_return']).reshape(-1, 1).astype(float)  # 2D array


model = LinearRegression() # Model Creation
model.fit(x, y)

                            # Coefficients Extraction
beta = model.coef_[0][0]   # slope
alpha = model.intercept_  # intercept

print("Library Linear Regression:")
print("Beta (slope):", beta)
print("Alpha (intercept):", alpha)
print("Based on one year data, BRACBANK moves {:.2f} times the market on average.".format(beta))

