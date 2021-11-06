import requests
from bs4 import BeautifulSoup

# NOTE(axolotl): the '-> str' at the end of each function specifies that this function returns a string.

url = ""
price = ""

def bitcoin_price() -> str:
    url = "https://coinmarketcap.com/currencies/bitcoin/markets/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})
    
    return price.text

def ethereum_price() -> str:
    url = "https://coinmarketcap.com/currencies/ethereum/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text

def binance_price() -> str:
    url = "https://coinmarketcap.com/currencies/binance-coin/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text

def tether_price() -> str:
    url = "https://coinmarketcap.com/currencies/tether/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text

def dogecoin_price() -> str:
    url = "https://coinmarketcap.com/currencies/dogecoin/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text

def bitrise_price() -> str:
    url = "https://coinmarketcap.com/currencies/bitrise-token/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text

def micropets_price() -> str:
    url = "https://coinmarketcap.com/currencies/micropets/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text

def shibazilla_price() -> str:
    url = "https://coinmarketcap.com/currencies/shibazilla/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text

def cardano_price() -> str:
    url = "https://coinmarketcap.com/currencies/cardano/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text

def xrp_price() -> str:
    url = "https://coinmarketcap.com/currencies/xrp/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text

def stellar_price() -> str:
    url = "https://coinmarketcap.com/currencies/stellar/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text

def sushiswap_price() -> str:
    url = "https://coinmarketcap.com/currencies/sushiswap/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})

    return price.text



