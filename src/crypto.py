import requests
from bs4 import BeautifulSoup
from rich import text
import mod_bootloader
import time

# NOTE(axolotl): the '-> str' at the end of each function specifies that this function returns a string.

url = ""
price = ""

def price(mod_id) -> str:
    url = mod_bootloader.dictionary_links(mod_id)
    url = url.replace("\n", "")
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find("div", {"class": "priceValue"})
    return price.text
