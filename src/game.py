import time
import os
import crypto
from datetime import datetime
# rich libaries
from rich import print
from rich.console import Console

console = Console()


# if this is showing a warning, ignore it, this is a pylance/vscode issue
# the program runs fine! \__(· _ · )__/
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


def sell_crypto():
    print("What Crypto do you want to sell?")
    time.sleep(1)
    # uglyyyyyyy
    # we need to create the variables so that they don't go out of scope in the statements below ↓
    btc_owned, eth_owned, binance_owned, tether_owned = "","","",""

    p_btc = saves_path_main + "bitcoin.txt"
    p_eth = saves_path_main + "ethereum.txt"
    p_binance = saves_path_main + "binance.txt"
    p_tether = saves_path_main + "tether.txt"

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

    print("1. Bitcoin:")
    print(f"Owned: [underline]{btc_owned}[/]\n")

    print("2. Ethereum:")
    print(f"Owned: [underline]{eth_owned}[/]\n")

    print("3. Binance Coin:")
    print(f"Owned: [underline]{binance_owned}[/]\n")

    print("4. Tether:")
    print(f"Owned: [underline]{tether_owned}[/]\n")

    sell_choice = input(": ")
    selling_name = ""
    selling = ""
    save_file_sell = ""
    if sell_choice == "1":
        selling_name = "Bitcoin"
        selling = btc_owned
        save_file_sell = saves_path_main + "bitcoin.txt"
    if sell_choice == "2":
        selling_name = "Ethereum"
        selling = eth_owned
        save_file_sell = saves_path_main + "ethereum.txt"
    if sell_choice == "3":
        selling_name = "Binance"
        selling = binance_owned
        save_file_sell = saves_path_main + "binance.txt"
    if sell_choice == "4":
        selling_name = "Tether"
        selling = tether_owned
        save_file_sell = saves_path_main + "tether.txt"

    time.sleep(2)
    print("Selected: " + selling_name + "\n" + "Owned: " + selling)
    console.print(f"How much [bold]{selling_name}[/] to sell?")
    sell_amount = str2float(input(": "))

    # Removing Crypto from Account
    # selling = float(selling) - float(sell_amount) <- what is this?!
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


    btc_owned, eth_owned, binance_owned, tether_owned = "","","",""

    p_btc = saves_path_main + "bitcoin.txt"
    p_eth = saves_path_main + "ethereum.txt"
    p_binance = saves_path_main + "binance.txt"
    p_tether = saves_path_main + "tether.txt"

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

    buy_choice = input(": ")

    #Just some declarations
    buying_name = ""
    buying = ""
    save_file_buy = ""

    if buy_choice == "1":
        price_crypto = crypto.bitcoin_price() 
        buying_name = "Bitcoin"
        buying = btc_owned
        save_file_buy = saves_path_main + "bitcoin.txt"
    elif buy_choice == "2":
        price_crypto = crypto.ethereum_price()
        buying_name = "Ethereum"
        buying = eth_owned
        save_file_buy = saves_path_main + "ethereum.txt"
    elif buy_choice == "3":
        price_crypto = crypto.binance_price()
        buying_name = "Binance"
        buying = binance_owned
        save_file_buy = saves_path_main + "binance.txt"
    elif buy_choice == "4":
        price_crypto = crypto.tether_price()
        buying_name = "Tether"
        buying = tether_owned
        save_file_buy = saves_path_main + "tether.txt"
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
        crypto_add_buy.write(str(float(buy_amount) + float(buying)))
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
