import time
import os
import crypto
from datetime import datetime
# rich libaries
from rich import print
from rich.console import Console

console = Console()


# if this is showing a warning, ignore it, this is a pylance/vscode issue
# the program runs fine! \__(· _ · )__/*
from str2float import str2float
import filer


main_run_path = os.path.dirname(os.path.abspath(__file__))

print("Debug Info:")
print(main_run_path)

saves_path_main = main_run_path + "/saves/"


def clear():
    console.clear()

def tutorial():
    print("Welcome to Cryptillionaire")
    time.sleep(0.5)
    print("In this game you need to invest into Crypto to get MONEY (€)\nby trading it")
    time.sleep(0.5)
    print("You are starting with 1000€ and work your way up to be the next millionaire")
    time.sleep(0.5)
    tutorial_answer = input(
        "Have you read the Text above? \nHint: type YES to procede: ")

    if tutorial_answer == "YES" or "yes" or "y" or "Y":
        os.mkdir(main_run_path + "/saves/")
        time.sleep(1)
        print("Making Saves Folder...")
        time.sleep(3)
        f_money_setup = open(saves_path_main + "/money.txt", 'w+')
        print("Adding Money to Bank Account...")
        time.sleep(2)
        f_money_setup.write("1000")
        f_money_setup.close()
        print("Finalizing...")
        time.sleep(2)
        f = open(saves_path_main + "/tutorial.txt", 'w+')
        f.write("Tutorial is Done")
        f.close()
        f_history_setup = open(saves_path_main + "/history.txt", 'w+')
        f_history_setup.write(str(datetime.now()) + "  Installed Cryptillionaire \n" )
        f_history_setup.close()
        print("Please Restart your Game to let it finish setting up")


def show_crypto():
    #Bitcoin Stats
    print("Bitcoin: ")
    console.print(f"[bold underline]{crypto.bitcoin_price()}[/]\n")

    #Ethereum Stats
    print("Ethereum: ")
    console.print(f"[bold underline]{crypto.ethereum_price()}[/]\n")

    #Binance Coin Stats
    print("Binance Coin: ")
    console.print(f"[bold underline]{crypto.binance_price()}[/]\n")

    #Tether Stats
    print("Tether: ")
    console.print(f"[bold underline]{crypto.tether_price()}[/]\n")

    #DogeCoin Stats
    print("DogeCoin: ")
    console.print(f"[bold underline]{crypto.dogecoin_price()}[/]\n")

    #Bitrise Stats
    print("Bitrise: ")
    console.print(f"[bold underline]{crypto.bitrise_price()}[/]\n")

    #Micropets Stats
    print("Mircopets: ")
    console.print(f"[bold underline]{crypto.micropets_price()}[/]\n")
    
    #Shibazilla Stats
    print("Shibazilla: ")
    console.print(f"[bold underline]{crypto.shibazilla_price()}[/]\n")

    #Cardano Stats
    print("Cardano: ")
    console.print(f"[bold underline]{crypto.cardano_price()}[/]\n")

    #XRP Stats
    print("XRP: ")
    console.print(f"[bold underline]{crypto.xrp_price()}[/]\n")

    #Stellar Stats
    print("Stellar: ")
    console.print(f"[bold underline]{crypto.stellar_price()}[/]\n")

    #Sushiswap Stats
    print("Sushiswap: ")
    console.print(f"[bold underline]{crypto.sushiswap_price()}[/]\n")








def sell_crypto():
    print("What Crypto do you want to sell?")
    time.sleep(1)
    # uglyyyyyyy
    # we need to create the variables so that they don't go out of scope in the statements below ↓
    btc_owned, eth_owned, binance_owned, tether_owned, doge_owned, bitrise_owned, micropets_owned, shibazilla_owned, cardano_owned, xrp_owned, stellar_owned, sushiswap_owned = "", "", "", "", "", "", "", "", "", "", "", ""

    p_btc = saves_path_main + "bitcoin.txt"
    p_eth = saves_path_main + "ethereum.txt"
    p_binance = saves_path_main + "binance.txt"
    p_tether = saves_path_main + "tether.txt"
    p_doge = saves_path_main + "tether.txt"
    p_bitrise = saves_path_main + "bitrise.txt"
    p_micropets = saves_path_main + "micropets.txt"
    p_shibazilla = saves_path_main + "shibazilla.txt"
    p_cardano = saves_path_main + "cardano.txt"
    p_xrp = saves_path_main + "xrp.txt"
    p_stellar = saves_path_main + "stellar.txt"
    p_sushiswap = saves_path_main + "sushiswap.txt"


    # ik very ugly but it should work
    if filer.filing(p_btc):
        btc_owned = filer.read_file(p_btc)
    elif filer.filing(p_btc, create_file=True):
        btc_owned = filer.read_file(p_btc)

    if filer.filing(p_eth):
        eth_owned = filer.read_file(p_eth)
    elif filer.filing(p_eth, True):
        eth_owned = filer.read_file(p_eth)

    if filer.filing(p_binance):
        binance_owned = filer.read_file(p_binance)
    elif filer.filing(p_binance, create_file=True):
        binance_owned = filer.read_file(p_binance)

    if filer.filing(p_tether):
        tether_owned = filer.read_file(p_tether)
    elif filer.filing(p_tether, create_file=True):
        tether_owned = filer.read_file(p_tether)

    
    if filer.filing(p_doge):
        doge_owned = filer.read_file(p_doge)
    elif filer.filing(p_doge, create_file=True):
        micropets_owned = filer.read_file(p_doge)

    if filer.filing(p_bitrise):
        bitrise_owned = filer.read_file(p_bitrise)
    elif filer.filing(p_doge, create_file=True):
        bitrise_owned = filer.read_file(p_bitrise)
    
    if filer.filing(p_micropets):
        micropets_owned = filer.read_file(p_micropets)
    elif filer.filing(p_micropets, create_file=True):
        micropets_owned = filer.read_file(p_micropets)

    
    if filer.filing(p_shibazilla):
        shibazilla_owned = filer.read_file(p_shibazilla)
    elif filer.filing(p_shibazilla, create_file=True):
        shibazilla_owned = filer.read_file(p_shibazilla)

    
    if filer.filing(p_cardano):
        cardano_owned = filer.read_file(p_cardano)
    elif filer.filing(p_cardano, create_file=True):
        cardano_owned = filer.read_file(p_cardano)

    
    if filer.filing(p_xrp):
        xrp_owned = filer.read_file(p_xrp)
    elif filer.filing(p_xrp, create_file=True):
        xrp_owned = filer.read_file(p_xrp)

    
    if filer.filing(p_stellar):
        stellar_owned = filer.read_file(p_stellar)
    elif filer.filing(p_stellar, create_file=True):
        stellar_owned = filer.read_file(p_stellar)

    
    if filer.filing(p_sushiswap):
        sushiswap_owned = filer.read_file(p_sushiswap)
    elif filer.filing(p_sushiswap, create_file=True):
        sushiswap_owned = filer.read_file(p_sushiswap)


    print("1. Bitcoin:")
    print(f"Owned: [underline]{btc_owned}[/]\n")

    print("2. Ethereum:")
    print(f"Owned: [underline]{eth_owned}[/]\n")

    print("3. Binance Coin:")
    print(f"Owned: [underline]{binance_owned}[/]\n")

    print("4. Tether:")
    print(f"Owned: [underline]{tether_owned}[/]\n")

    print("4. Dogecoin:")
    print(f"Owned: [underline]{doge_owned}[/]\n")

    print("4. Bitrise:")
    print(f"Owned: [underline]{bitrise_owned}[/]\n")

    print("4. Micropets:")
    print(f"Owned: [underline]{micropets_owned}[/]\n")

    print("4. Shibazilla:")
    print(f"Owned: [underline]{shibazilla_owned}[/]\n")

    print("4. Cardano:")
    print(f"Owned: [underline]{cardano_owned}[/]\n")

    print("4. XRP:")
    print(f"Owned: [underline]{xrp_owned}[/]\n")

    print("4. Stellar:")
    print(f"Owned: [underline]{stellar_owned}[/]\n")

    print("4. Sushiswap:")
    print(f"Owned: [underline]{sushiswap_owned}[/]\n")

    sell_choice = input(": ")
    selling_name = ""
    selling = ""
    save_file_sell = ""
    if sell_choice == "1":
        selling_name = "Bitcoin"
        selling = btc_owned
        save_file_sell = p_btc
    if sell_choice == "2":
        selling_name = "Ethereum"
        selling = eth_owned
        save_file_sell = p_eth
    if sell_choice == "3":
        selling_name = "Binance"
        selling = binance_owned
        save_file_sell = p_binance
    if sell_choice == "4":
        selling_name = "Tether"
        selling = tether_owned
        save_file_sell = p_tether
    if sell_choice == "5":
        selling_name = "Dogecoin"
        selling = doge_owned
        save_file_sell = p_doge
    if sell_choice == "6":
        selling_name = "Bitrise"
        selling = bitrise_owned
        save_file_sell = p_bitrise
    if sell_choice == "7":
        selling_name = "Micropets"
        selling = micropets_owned
        save_file_sell = p_micropets
    if sell_choice == "8":
        selling_name = "Shibazilla"
        selling = shibazilla_owned
        save_file_sell = p_shibazilla
    if sell_choice == "9":
        selling_name = "Cardano"
        selling = cardano_owned
        save_file_sell = p_cardano
    if sell_choice == "10":
        selling_name = "XRP"
        selling = xrp_owned
        save_file_sell = p_xrp
    if sell_choice == "11":
        selling_name = "Stellar"
        selling = stellar_owned
        save_file_sell = p_stellar
    if sell_choice == "12":
        selling_name = "Sushiswap"
        selling = sushiswap_owned
        save_file_sell = p_sushiswap
    

    time.sleep(2)
    print("Selected: " + selling_name + "\n" + "Owned: " + selling)
    console.print(f"How much [bold]{selling_name}[/] to sell?")
    sell_amount = str2float(input(": "))

    # Removing Crypto from Account
    # selling = float(selling) - float(sell_amount) <- what is this?! <- IDK, Dont ask me, ask Python.
    if float(selling) - float(sell_amount) < 0:
        console.print("[red on white]Not enough Crypto![/]")
        selling = float(selling) + float(sell_amount)

    elif float(selling) - float(sell_amount) >= 0:
        selling = float(selling) - float(sell_amount)
        time.sleep(1)
        console.print("[red on white]Press ENTER to confirm sell...[/]")
        input()
        f_confirm_sell_save = open(save_file_sell, 'w')
        f_confirm_sell_save.write(str(selling))
        f_confirm_sell_save.close()

        # close the fucking files XD
        price_current_sell = 0.0
        if sell_choice == "1":
            price_current_sell = str2float(crypto.bitcoin_price())
        elif sell_choice == "2":
            price_current_sell = str2float(crypto.ethereum_price())
        elif sell_choice == "3":
            price_current_sell = str2float(crypto.binance_price())
        elif sell_choice == "4":
            price_current_sell = str2float(crypto.tether_price())
        elif sell_choice == "5":
            price_current_sell = str2float(crypto.dogecoin_price())
        elif sell_choice == "6":
            price_current_sell = str2float(crypto.bitrise_price())
        elif sell_choice == "7":
            price_current_sell = str2float(crypto.micropets_price())
        elif sell_choice == "8":
            price_current_sell = str2float(crypto.shibazilla_price())
        elif sell_choice == "9":
            price_current_sell = str2float(crypto.cardano_price())
        elif sell_choice == "10":
            price_current_sell = str2float(crypto.xrp_price())
        elif sell_choice == "11":
            price_current_sell = str2float(crypto.stellar_price())
        elif sell_choice == "12":
            price_current_sell = str2float(crypto.sushiswap_price())


        money_adding_sell = price_current_sell * sell_amount

        f_money_sell = open(saves_path_main + "money.txt", 'r')
        money_sell_bank = str2float(f_money_sell.read())
        f_money_sell.close()

        f_money_sell = open(saves_path_main + "money.txt", "w")
        f_money_sell.write(str(money_sell_bank + money_adding_sell))
        f_money_sell.close()
        
        print(f"You got €{str(money_adding_sell)} from selling {str(sell_amount)} {selling_name}")
        f_history = open(saves_path_main + "/history.txt", 'a')
        f_history.write(str(datetime.now()) + f" : Sold {sell_amount} {selling_name} for {money_adding_sell}\n" )
        f_history.close()
        

        
def show_history():
    f_show_history = open(saves_path_main + "/history.txt", 'r')
    for line in f_show_history:
        print(line)
    console.print("Press [bold]ENTER[/] to return to Main Menu")
    input()


def buy_crypto():
    print("Select Cryptocurrency:")
    print("1. Bitcoin")
    console.print(f"Price: [underline]{crypto.bitcoin_price()}[/]")
    print("2. Ethereum")
    console.print(f"Price: [underline]{crypto.ethereum_price()}[/]")
    print("3. Binance")
    console.print(f"Price: [underline]{crypto.binance_price()}[/]")
    print("4. Tether")
    console.print(f"Price: [underline]{crypto.tether_price()}[/]")
    print("5. Dogecoin")
    console.print(f"Price: [underline]{crypto.tether_price()}[/]")
    print("6. Bitrise")
    console.print(f"Price: [underline]{crypto.tether_price()}[/]")
    print("7. Micropets")
    console.print(f"Price: [underline]{crypto.tether_price()}[/]")
    print("8. Shibazilla")
    console.print(f"Price: [underline]{crypto.tether_price()}[/]")
    print("9. Cardano")
    console.print(f"Price: [underline]{crypto.tether_price()}[/]")
    print("10. XRP")
    console.print(f"Price: [underline]{crypto.tether_price()}[/]")
    print("11. Stellar")
    console.print(f"Price: [underline]{crypto.tether_price()}[/]")
    print("12. Sushiswap")
    console.print(f"Price: [underline]{crypto.tether_price()}[/]")

    btc_owned, eth_owned, binance_owned, tether_owned, doge_owned, bitrise_owned, micropets_owned, shibazilla_owned, cardano_owned, xrp_owned, stellar_owned, sushiswap_owned = "", "", "", "", "", "", "", "", "", "", "", ""

    p_btc = saves_path_main + "bitcoin.txt"
    p_eth = saves_path_main + "ethereum.txt"
    p_binance = saves_path_main + "binance.txt"
    p_tether = saves_path_main + "tether.txt"
    p_doge = saves_path_main + "tether.txt"
    p_bitrise = saves_path_main + "bitrise.txt"
    p_micropets = saves_path_main + "micropets.txt"
    p_shibazilla = saves_path_main + "shibazilla.txt"
    p_cardano = saves_path_main + "cardano.txt"
    p_xrp = saves_path_main + "xrp.txt"
    p_stellar = saves_path_main + "stellar.txt"
    p_sushiswap = saves_path_main + "sushiswap.txt"

    # ik very ugly but it should work x2
    if filer.filing(p_btc):
        btc_owned = filer.read_file(p_btc)
    elif filer.filing(p_btc, create_file=True):
        btc_owned = filer.read_file(p_btc)

    if filer.filing(p_eth):
        eth_owned = filer.read_file(p_eth)
    elif filer.filing(p_eth, True):
        eth_owned = filer.read_file(p_eth)

    if filer.filing(p_binance):
        binance_owned = filer.read_file(p_binance)
    elif filer.filing(p_binance, create_file=True):
        binance_owned = filer.read_file(p_binance)

    if filer.filing(p_tether):
        tether_owned = filer.read_file(p_tether)
    elif filer.filing(p_tether, create_file=True):
        tether_owned = filer.read_file(p_tether)

    
    if filer.filing(p_doge):
        doge_owned = filer.read_file(p_doge)
    elif filer.filing(p_doge, create_file=True):
        micropets_owned = filer.read_file(p_doge)

    if filer.filing(p_bitrise):
        bitrise_owned = filer.read_file(p_bitrise)
    elif filer.filing(p_doge, create_file=True):
        bitrise_owned = filer.read_file(p_bitrise)
    
    if filer.filing(p_micropets):
        micropets_owned = filer.read_file(p_micropets)
    elif filer.filing(p_micropets, create_file=True):
        micropets_owned = filer.read_file(p_micropets)

    
    if filer.filing(p_shibazilla):
        shibazilla_owned = filer.read_file(p_shibazilla)
    elif filer.filing(p_shibazilla, create_file=True):
        shibazilla_owned = filer.read_file(p_shibazilla)

    
    if filer.filing(p_cardano):
        cardano_owned = filer.read_file(p_cardano)
    elif filer.filing(p_cardano, create_file=True):
        cardano_owned = filer.read_file(p_cardano)

    
    if filer.filing(p_xrp):
        xrp_owned = filer.read_file(p_xrp)
    elif filer.filing(p_xrp, create_file=True):
        xrp_owned = filer.read_file(p_xrp)

    
    if filer.filing(p_stellar):
        stellar_owned = filer.read_file(p_stellar)
    elif filer.filing(p_stellar, create_file=True):
        stellar_owned = filer.read_file(p_stellar)

    
    if filer.filing(p_sushiswap):
        sushiswap_owned = filer.read_file(p_sushiswap)
    elif filer.filing(p_sushiswap, create_file=True):
        sushiswap_owned = filer.read_file(p_sushiswap)

    buy_choice = input(": ")

    #Just some declarations
    buying_name = ""
    buying = ""
    save_file_buy = ""

    if buy_choice == "1":
        price_crypto = crypto.bitcoin_price() 
        buying_name = "Bitcoin"
        buying = btc_owned
        save_file_buy = p_btc
    elif buy_choice == "2":
        price_crypto = crypto.ethereum_price()
        buying_name = "Ethereum"
        buying = eth_owned
        save_file_buy = p_eth
    elif buy_choice == "3":
        price_crypto = crypto.binance_price()
        buying_name = "Binance"
        buying = binance_owned
        save_file_buy = p_binance
    elif buy_choice == "4":
        price_crypto = crypto.tether_price()
        buying_name = "Tether"
        buying = (tether_owned)
        save_file_buy = p_eth
    elif buy_choice == "5":
        price_crypto = crypto.dogecoin_price()
        buying_name = "Dogecoin"
        buying = (doge_owned)
        save_file_buy = p_doge
    elif buy_choice == "6":
        price_crypto = crypto.bitrise_price()
        buying_name = "Bitrise"
        buying = (bitrise_owned)
        save_file_buy = p_bitrise
    elif buy_choice == "7":
        price_crypto = crypto.micropets_price()
        buying_name = "Micropets"
        buying = (micropets_owned)
        save_file_buy = p_micropets
    elif buy_choice == "8":
        price_crypto = crypto.shibazilla_price()
        buying_name = "Shibazilla"
        buying = (shibazilla_owned)
        save_file_buy = p_shibazilla
    elif buy_choice == "9":
        price_crypto = crypto.cardano_price()
        buying_name = "Cardano"
        buying = (cardano_owned)
        save_file_buy = p_cardano
    elif buy_choice == "10":
        price_crypto = crypto.xrp_price()
        buying_name = "XRP"
        buying = (xrp_owned)
        save_file_buy = p_xrp
    elif buy_choice == "11":
        price_crypto = crypto.stellar_price()
        buying_name = "Stellar"
        buying = (stellar_owned)
        save_file_buy = p_stellar
    elif buy_choice == "12":
        price_crypto = crypto.sushiswap_price()
        buying_name = "Sushiswap"
        buying = (sushiswap_owned)
        save_file_buy = p_sushiswap
    else:
        console.print("[red on white]Selection not Valid![/]")
        time.sleep(1)
        console.print("[red on white]Exiting to Main Menu![/]")
        time.sleep(2)
        main_menu()

    time.sleep(2)
    print("Selected: " + buying_name + "\n" + "Owned: " + buying)
    print(f"How much {buying_name} to Buy?")
    buy_amount = str2float(input(": "))


    f_money_buy = open(saves_path_main + "money.txt", 'r')
    money_bank = str2float(f_money_buy.read())
    f_money_buy.close()
    price_crypto = price_crypto.replace("$", "")

    if float(money_bank) - str2float(price_crypto) < 0:
        print("Not enough Money!")
        print("Exiting to Main Menu!")
        time.sleep(3)
        main_menu()

    elif float(money_bank) - str2float(price_crypto) >= 0:
        time.sleep(1)
        print(f"INFO: Buying {buy_amount} {buying_name} for {price_crypto} €")
        time.sleep(3)
        input("Press ENTER to confirm sell...")


        money_removing_buy = str2float(price_crypto) * float(buy_amount)


        f_money_buy = open(saves_path_main + "money.txt", "w")
        f_money_buy.write(str(money_bank - money_removing_buy))
        f_money_buy.close()

        crypto_add_buy = open(save_file_buy, "w")
        crypto_add_buy.write(str(float(buy_amount) + str2float(buying)))
        crypto_add_buy.close()
        print("Buy Process Succedeed! \n Exiting to Main Menu!")

        f_history = open(saves_path_main + "/history.txt", 'a')
        f_history.write(str(datetime.now()) + f" : Bought {buy_amount} {buying_name} for {money_removing_buy}\n" )
        f_history.close()

        time.sleep(2)
        main_menu()






def main_menu():
    clear()
    print("Welcome to Cryptillionaire")
    time.sleep(0.4)
    print("Available Choices:")
    time.sleep(0.4)
    print("1: Show Crypto Prices")
    time.sleep(0.3)
    print("2: Sell Crpto")
    time.sleep(0.3)
    print("3: Buy Crypto")
    time.sleep(0.3)
    print("4: View History")
    time.sleep(0.3)
    print("5: Exit")

    menu_choice = input("\n: ")
    if menu_choice == "1":
        show_crypto()
        input("Press ENTER to return to Main Menu")
        main_menu()

    if menu_choice == "2":
        sell_crypto()
        input("Press ENTER to return to Main Menu")
        main_menu()

    if menu_choice == "3":
        buy_crypto()

    if menu_choice == "4":
        show_history()

    if menu_choice == "5":
        print("Exiting...")
        time.sleep(3)
        exit()


if filer.filing(saves_path_main + "tutorial.txt", create_file=False):
    main_menu()
else:
    tutorial()
