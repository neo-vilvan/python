import warnings
warnings.filterwarnings('ignore')
import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import yfinance as yf
import matplotlib.dates as mdates

prices_df = yf.download(tickers=['MSFT'],
                        start='2018-01-01',
                        end=dt.date.today())

prices_df['return'] = np.log(prices_df['Adj Close']).diff()

prices_df = prices_df.dropna()

print(prices_df)


# Plot the data
fig, ax = plt.subplots(figsize=(12, 8))

# Plot Adjusted Close price
ax.plot(prices_df.index, prices_df['Adj Close'], label='Adjusted Close')

# Plot daily returns
ax.plot(prices_df.index, prices_df['return'], label='Daily Returns')

# Set axis labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Price/Return')
ax.set_title('Microsoft Stock Price and Returns')

# Format x-axis ticks as dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Rotate x-axis tick labels for better readability
plt.xticks(rotation=45)

# Add legend to the plot
ax.legend()

# Display the plot
#plt.show()






model = sm.tsa.MarkovRegression(endog=prices_df['return'],
                                k_regimes=2,
                                trend='c',
                                switching_variance=True)

result = model.fit()

regime_probability = result.smoothed_marginal_probabilities[1].to_frame('regime')

regime_probability.plot(figsize=(16,4))

plt.title('MSFT Volatility Regimes')

plt.axhline(.5, color='black')

plt.ylabel('Low/High Volatility')

plt.show()