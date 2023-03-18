import pandas as pd # The pandas library for data analysis and manipulation.
import requests as requests # Requests for making network connections.
from bs4 import BeautifulSoup # For extracting data from HTML and XML docs.

titles = []
urls = []
time = []

web_url = "https://parsehub.com/sandbox/showtimes" # Target website
fetched_page = requests.get(web_url) # Fetching the page


beautifulsoup = BeautifulSoup(fetched_page.text, "html.parser")


for movie in beautifulsoup.find_all('a','title'):
 titles.append(movie.string)
 urls.append(movie.get('href'))


print(titles)

#for showtime in beautifulsoup.find_all('span','imax'):
# time.append(showtime.string)

#raw_data={
# 'movie_title':titles,
# 'show_time':time,
# 'image_url':urls
#}


#dataframe = pd.DataFrame(raw_data, columns=['movie_title', 'show_time', 'image_url'])

#print(dataframe)

#dataframe.to_csv('raw_data.csv', index=False)