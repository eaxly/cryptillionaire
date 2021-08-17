import requests
from bs4 import BeautifulSoup

# NOTE(axolotl): the '-> str' at the end of each function specifies that this function returns a string.

def bitcoin_price() -> str:
    url_btc = "https://coinmarketcap.com/currencies/bitcoin/markets/"
    req = requests.get(url_btc)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_btc = soup.find("div", {"class": "priceValue___11gHJ"})
    
    return price_btc.text

def ethereum_price() -> str:
    url_eth = "https://coinmarketcap.com/currencies/ethereum/"
    req = requests.get(url_eth)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_eth = soup.find("div", {"class": "priceValue___11gHJ"})

    return price_eth.text

def binance_price() -> str:
    url_bnb = "https://coinmarketcap.com/currencies/binance-coin/"
    req = requests.get(url_bnb)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_bnb = soup.find("div", {"class": "priceValue___11gHJ"})

    return price_bnb.text

def tether_price() -> str:
    url_usdt = "https://coinmarketcap.com/currencies/tether/"
    req = requests.get(url_usdt)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_usdt = soup.find("div", {"class": "priceValue___11gHJ"})

    return price_usdt.text
