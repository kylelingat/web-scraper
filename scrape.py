import schedule
import time
from bs4 import BeautifulSoup
import urllib.request
from time import gmtime, strftime


def scrapePrice():
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    name_box = strftime("As Of " + "%m/%d/%Y %H:%M", gmtime()) + ", the Bitcoin price is" + " $" + soup.find(attrs={"class": "text-large2"}).get_text()
    text = name_box.encode()
    print(text)
    f = open('bitcoinPrice.txt', 'wb')
    f.write(text)
    f.close()
    print('Price saved to bitcoinPrice.txt')


schedule.every(1).minutes.do(scrapePrice)

while 1:
    schedule.run_pending()
    time.sleep(1)
