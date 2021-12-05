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

def register_mods():
    flush_mod_storage()
    count = 0
    modfiles = [f for f in listdir(modfolder) if isfile(join(modfolder, f))]
    mods_count = len(modfiles)
    while mods_count > count:
        first_modfile = open(modfolder + "/" + modfiles[count], 'r')
        first_modfile_read = first_modfile.readlines()

        crypto_mod_name = open(mod_storage_dir + "/crypto_names.txt", 'a')
        crypto_price_link = open(mod_storage_dir + "/crypto_price_links.txt", 'a')


        crypto_mods_list = []

        for line in first_modfile_read:
            crypto_mods_list.append(line)

        crypto_mod_name.write(crypto_mods_list[0])
        crypto_price_link.write(crypto_mods_list[1] + "\n")
        count = count + 1
        first_modfile.close()
        crypto_mod_name.close()
        crypto_price_link.close()

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
