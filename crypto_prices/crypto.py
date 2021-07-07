import requests
from bs4 import BeautifulSoup


def bitcoin_price():
    #Bitcoin Stats
    url_btc = "https://coinmarketcap.com/currencies/bitcoin/markets/"
    req = requests.get(url_btc)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_btc = soup.find("div", {"class": "priceValue___11gHJ"})
    print(price_btc.text)

def ethereum_price():
    #Ethereum Stats
    url_eth = "https://coinmarketcap.com/currencies/ethereum/"
    req = requests.get(url_eth)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_eth = soup.find("div", {"class": "priceValue___11gHJ"})
    print(price_eth.text)

def binance_price():
    #Binance Coin Stats
    url_bnb = "https://coinmarketcap.com/currencies/binance-coin/"
    req = requests.get(url_bnb)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_bnb = soup.find("div", {"class": "priceValue___11gHJ"})
    print(price_bnb.text)

def tether_price():
        #Tether Stats
    url_usdt = "https://coinmarketcap.com/currencies/tether/"
    req = requests.get(url_usdt)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_usdt = soup.find("div", {"class": "priceValue___11gHJ"})
    print(price_usdt.text)