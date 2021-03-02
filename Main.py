from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
from pprint import pprint

def main():
    driver = webdriver.Firefox() # webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    products=[] #List to store name of the product
    prices=[] #List to store price of the product
    ratings=[] #List to store rating of the product
    driver.get("https://www.flipkart.com/computers/monitors/pr?sid=6bo,9no&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_0a4329f6-060a-460c-aff5-e710c5660a0e_1_372UD5BXDFYS_MC.ECL5SFI77NSY&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Electronics~Computer%2BPeripherals~Monitors_ECL5SFI77NSY&cid=ECL5SFI77NSY")

    # soup = BeautifulSoup(driver.page_source, 'html.parser')

    # maxPageCount = int(html_soup.find('a', class_ = 'totalPageNum').text)+1
    content = driver.page_source

    i = 0

    while True:
        # TODO might be a selenium method
        time.sleep(3) # per stackoverflow, there might be a race condition in the driver and this prevents it https://stackoverflow.com/questions/49734915/failed-to-decode-response-from-marionette-message-in-python-firefox-headless-s
        content = driver.page_source
        scrapPage(content, products, prices, ratings)
        i += 1
        print('page: ', i)

        try:
            driver.find_element_by_link_text('NEXT').click()
        except:
            print('Next link was not found')
            break


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

def scrapPage(content, products, prices, ratings):
    soup = BeautifulSoup(content)
    for a in soup.findAll(name='a',href=True, attrs={'class':'_1fQZEK'}):
        name=a.find('div', attrs={'class':'_4rR01T'})
        price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        rating=a.find('div', attrs={'class':'_3LWZlK'})
        products.append(name.text)
        prices.append(price.text)
        if rating == None:
            ratings.append('No Ratings')
        else:
            ratings.append(rating.text) 

if __name__ == "__main__":
    main()