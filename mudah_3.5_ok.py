import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

house_titles = []
house_prices = []

# Set the URL to fetch
url = "https://www.mudah.my/list?category=2001&price=500000-750000&region=12&sortby=price_asc&type=sell"

# Set the headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

# Send a GET request to the URL with the headers
fetched_page = requests.get(url, headers=headers)

# Parse the fetched_page HTML using BeautifulSoup
parsed_page = BeautifulSoup(fetched_page.content, 'html.parser')

# Find all the house listings on the page
house_listings = parsed_page.find_all(lambda tag: tag.name == "div" and "listing-ad-item" in tag.attrs.get("data-testid", ""))

# Extract the titles and prices from the house listings
for house_listing in house_listings:
    house_titles.append(house_listing.find("a", attrs={"title": True}).get("title"))
    house_prices.append(int(re.sub("[^0-9]", "", house_listing.find("div", class_=re.compile(r"^sc-j")).text)))

raw_data = {
    "House Name": house_titles,
    "House Prices": house_prices
}

dataframe = pd.DataFrame(raw_data, columns=["House Name", "House Prices"])
print(dataframe)

dataframe.to_csv('mudah_data.csv', index=False)