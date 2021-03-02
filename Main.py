from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from pprint import pprint

driver = webdriver.Firefox() # webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/computers/monitors/pr?sid=6bo,9no&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_0a4329f6-060a-460c-aff5-e710c5660a0e_1_372UD5BXDFYS_MC.ECL5SFI77NSY&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Electronics~Computer%2BPeripherals~Monitors_ECL5SFI77NSY&cid=ECL5SFI77NSY")

time.sleep(3) # per stackoverflow, there might be a race condition in the driver and this prevents it https://stackoverflow.com/questions/49734915/failed-to-decode-response-from-marionette-message-in-python-firefox-headless-s
content = driver.page_source
soup = BeautifulSoup(content)
# print(soup.prettify()
# print('all class: _1fQZEK')
# # print(soup.findAll('a',href=True, attrs={'class':'_13oc-S'}))
# pprint(soup.findAll(name='a',href=True, attrs={'class':'_1fQZEK'}))

for a in soup.findAll(name='a',href=True, attrs={'class':'_1fQZEK'}): # _1AtVbE col-12-12
    name=a.find('div', attrs={'class':'_4rR01T'})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 

# TODO BUG sometimes the thing just desnt load...is it the sleep line?
print('\nproducts')
pprint(products) # matches the order of the web page
temp = {'Product Name':products,'Price':prices,'Rating':ratings}
print('\ntemp')
print(temp)
df = pd.DataFrame(temp) # TODO this matches the order of the html, but witout the "temp" it doesnt...

# df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) # TODO why does this change the ordering of products? its not sorted on anything I can see
print('\ndf')
print(df)
df.to_csv('products.csv', index=False, encoding='utf-8')
