from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def scrape():
    # var init
    obj = {}
    studioSale = []
    studioRent = []
    apartmentSale = []
    apartmentRent = []

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
            type_ = None
            area = span_area[0].text
            price = span_price[0].text
            href = a[0]['href']

            if 'garsoniere-de-vanzare' in href:
                type_ = 'studioSale'
            if 'apartamente-de-vanzare' in href:
                type_ = 'apartmentSale'
            if 'garsoniere-de-inchiriat' in href:
                type_ = 'studioRent'
            if 'apartamente-de-inchiriat' in href:
                type_ = 'apartmentRent'
            if type_ is None:
                continue

            price = price.replace(" €/mp",'')
            pair = {area: {'price':price}}

            # build list
            if type_ == 'studioSale':
                studioSale.append(pair)
            if type_ == 'apartmentSale':
                apartmentSale.append(pair)
            if type_ == 'studioRent':
                studioRent.append(pair)
            if type_ == 'apartmentRent':
                apartmentRent.append(pair)

            obj['studioSale'] = studioSale
            obj['apartmentSale'] = apartmentSale
            obj['studioRent'] = studioRent
            obj['apartmentRent'] = apartmentRent

    return obj

