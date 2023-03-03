import requests
from bs4 import BeautifulSoup
import urllib.request

def getdata(url):
    r = requests.get(url)
    return r.text

htmldata = getdata("https://www.nationalgeographic.co.uk/space/2023/01/asteroids-vs-comets-how-do-they-differ-and-do-they-pose-a-threat-to-earth")
soup = BeautifulSoup(htmldata, 'html.parser')

test = list()
for item in soup.find_all('img'):
    print(item['src'])
    test.append(item.get('src'))

for i in range(len(test)):
    urllib.request.urlretrieve(test[i], str(i)+".jpg")