from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#url of the page we want to scrape 
url = "https://www.adamchoi.co.uk/teamgoals/detailed"

#init the driver
driver = webdriver.Chrome('./chromedriver')

#a version of Chrome will appear on the desktop
driver.get(url)

time.sleep(5)
all_matches_button = driver.find_element('//label[@analytics-event="All matches"]')
all_matches_button.click()


#hold until page loaded
time.sleep(5)

#driver.quit()
#hold until page loaded

