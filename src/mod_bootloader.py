import os
from os import listdir
from os.path import isfile, join
import filer as filer


modloader_dir = os.path.dirname(os.path.abspath(__file__))
modfolder = modloader_dir + "/mods/"
mod_storage_dir = modloader_dir + "/mod_storage"

def flush_mod_storage():
    crypto_mod_name = open(mod_storage_dir + "/crypto_names.txt", 'w')
    crypto_mod_price = open(mod_storage_dir + "/crypto_price_links.txt", 'w')
    crypto_mod_name.write("")
    crypto_mod_name.close()
    crypto_mod_price.write("")
    crypto_mod_price.close()


def init():
    os.mkdir(modloader_dir + "/mod_storage")
    filer.filing(mod_storage_dir + "/crypto_names.txt", create_file=True)
    filer.filing(mod_storage_dir + "/crypto_price_links.txt", create_file=True)
    filer.filing(modloader_dir + "/initFlag", create_file=True)
    os.mkdir(modloader_dir + "/mods")

def register_mods():
    flush_mod_storage()
    count = 0
    modfiles = [f for f in listdir(modfolder) if isfile(join(modfolder, f))]
    mods_count = len(modfiles)

    # Addng Default Mods:
    crypto_mod_name = open(mod_storage_dir + "/crypto_names.txt", 'a')
    crypto_price_link = open(mod_storage_dir + "/crypto_price_links.txt", 'a')
    crypto_mod_name.write("Bitcoin" + "\n")
    crypto_price_link.write("https://coinmarketcap.com/currencies/bitcoin/" + "\n")
    crypto_mod_name.write("Ethereum" + "\n")
    crypto_price_link.write("https://coinmarketcap.com/currencies/ethereum/" + "\n")
    crypto_mod_name.write("Binance" + "\n")
    crypto_price_link.write("https://coinmarketcap.com/currencies/binance-coin/" + "\n")
    crypto_mod_name.write("Dogecoin" + "\n")
    crypto_price_link.write("https://coinmarketcap.com/currencies/dogecoin/" + "\n")
    crypto_mod_name.close()
    crypto_price_link.close()
    while mods_count > count:
        old_crypto_names_list = []



        # Reading all Mods that are already in the crypto_names.txt file (Duplicate Detection)
        old_crypto_names = open(mod_storage_dir + "/crypto_names.txt", 'r')
        old_crypto_names_read = old_crypto_names.readlines()
        for line in old_crypto_names_read:
            old_crypto_names_list.append(line)
        old_crypto_names.close()
        crypto_mod_name = open(mod_storage_dir + "/crypto_names.txt", 'a')
        crypto_price_link = open(mod_storage_dir + "/crypto_price_links.txt", 'a')
        first_modfile = open(modfolder + "/" + modfiles[count], 'r')
        first_modfile_read = first_modfile.readlines()
        
        crypto_mods_list = []

        for line in first_modfile_read:
            crypto_mods_list.append(line)
        if old_crypto_names_list.count(crypto_mods_list[0]) > 0 :
            print(f"Duplicate Mod Found! --> Skipping: {crypto_mods_list[0]}")
        else:
            crypto_mod_name.write(crypto_mods_list[0])
            crypto_price_link.write(crypto_mods_list[1] + "\n")
            first_modfile.close()
            crypto_mod_name.close()
            crypto_price_link.close()
        count = count + 1

def dictionary_links(mod_index):
    crypto_price_link = open(mod_storage_dir + "/crypto_price_links.txt", 'r')

    crypto_links_list = []

    for crypto_link in crypto_price_link.readlines():
        crypto_links_list.append(crypto_link)
        
    return crypto_links_list[mod_index]
    

def dictionary_names(mod_index):
    crypto_mod_name = open(mod_storage_dir + "/crypto_names.txt", 'r')

    crypto_names_list = []
    
    for crypto_name in crypto_mod_name.readlines():
        crypto_names_list.append(crypto_name)
    
    return crypto_names_list[mod_index]


def handshake():
    modfiles = [f for f in listdir(modfolder) if isfile(join(modfolder, f))]
    mods_count = len(modfiles)
    return mods_count
