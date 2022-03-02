from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json

def scrape():
    # var init
    prices = []

    # set up scraper
    url = 'https://compariimobiliare.ro/pret-imobil'
    response = Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    webpage = urlopen(response).read()
    soup = BeautifulSoup(webpage, "html.parser")
    lis = soup.find_all("li")

    # navigate DOM, get area:price pairs
    for li in lis:
        a = li.find_all('a')
        span_area = li.find_all('span',{"class":"area-name"})
        span_price = li.find_all('span',{"class":"area-price"})
        if span_area:
            rooms = 0
            area = span_area[0].text
            price = span_price[0].text
            href = a[0]['href']
            if 'garsoniere-de-vanzare' in href:
                rooms = 1
                scope = 'sale'
            if 'apartamente-de-vanzare' in href:
                rooms = 2
                scope = 'sale'
            if 'garsoniere-de-inchiriat' in href:
                rooms = 1
                scope = 'rent'
            if 'apartamente-de-inchiriat' in href:
                rooms = 2
                scope = 'rent'
            if rooms == 0:
                continue
            price = price.replace(" €/mp",'')
            pair = {area: {'price':price, 'scope':scope ,'rooms':rooms}}
            prices.append(pair)
    prices = json.dumps(prices)
    return prices




