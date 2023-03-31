import pandas_ta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt
import matplotlib.dates as mdates

prices_df = yf.download(tickers= 'tsla', start='2019-01-01', end=dt.date.today())
prices_df['stoch_k'] = pandas_ta.stochrsi(close=prices_df['Adj Close'], length=20).iloc[:,0]
prices_df['stoch_d'] = pandas_ta.stochrsi(close=prices_df['Adj Close'], length=20).iloc[:,1]
prices_df['bb_lower'] = pandas_ta.bbands(close=prices_df['Adj Close'], length=20).iloc[:,0]
prices_df['bb_upper'] = pandas_ta.bbands(close=prices_df['Adj Close'], length=20).iloc[:,2]
prices_df['forward_1d'] = prices_df['Adj Close'].pct_change(1).shift(-1)
print(prices_df)

# Plot the data
fig, ax = plt.subplots(figsize=(12, 8))

# Plot Adjusted Close price
ax.plot(prices_df.index, prices_df['Adj Close'], label='Adjusted Close')

# Plot Bollinger Bands
ax.plot(prices_df.index, prices_df['bb_lower'], label='Lower Bollinger Band')
ax.plot(prices_df.index, prices_df['bb_upper'], label='Upper Bollinger Band')

# Plot Stochastic RSI
ax.plot(prices_df.index, prices_df['stoch_k'], label='Stochastic RSI K')
ax.plot(prices_df.index, prices_df['stoch_d'], label='Stochastic RSI D')

# Set axis labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Tesla Stock Price')

# Format x-axis ticks as dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Rotate x-axis tick labels for better readability
plt.xticks(rotation=45)

# Add legend to the plot
ax.legend()

# Display the plot
plt.show()
