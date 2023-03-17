import pycoingecko
import matplotlib.pyplot as plt
import datetime

# Initialize CoinGecko API client
coinGecko = pycoingecko.CoinGeckoAPI()

# Get historical price data for Bitcoin
btc_data = coinGecko.get_coin_market_chart_by_id('bitcoin', 'usd', '365days')
# Extract the dates and prices from the data
dates = [data[0] for data in btc_data['prices']]
# convert unix timestamp to datetime
dates = [
    datetime.datetime.fromtimestamp(date/1000)
    for date in dates
]
prices = [data[1] for data in btc_data['prices']]
# Plot the data
plt.plot(dates, prices)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Historical Bitcoin Price (USD)')
plt.show()