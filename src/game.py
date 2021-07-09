import time
import os.path
import crypto

# if this is showing a warning, ignore it, this is a pylance/vscode issue
# the program runs fine! \__(· _ · )__/
from str2float import str2float

# import os
# import html2text


main_run_path = os.path.dirname(os.path.abspath(__file__))

print("Debug Info:")
print(main_run_path)

saves_path_main = main_run_path + "/saves/"


def tutorial():
    print("Welcome to Cryptillionaire")
    time.sleep(0.5)
    print("In this game you need to invest into Crypto to get MONEY (§)\nby trading it")
    time.sleep(0.5)
    print("You are starting with 1000$ and work your way up to be the next millionaire")
    time.sleep(0.5)
    tutorial_answer = input(
        "Have you read the Text above? \n Hint: type YES to procede: ")
    if tutorial_answer == "YES":
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
        print("Please Restart your Game to let it finish setting up")


def show_cypto():
    #Bitcoin Stats
    print("Bitcoin: ")
    print(crypto.bitcoin_price() + "\n")

    #Ethereum Stats
    print("Ethereum: ")
    print(crypto.ethereum_price() + "\n")

    #Binance Coin Stats
    print("Binance Coin: ")
    print(crypto.binance_price() + "\n")

    #Tether Stats
    print("Tether: ")
    print(crypto.tether_price() + "\n")


def sell_crypto():
    print("What Crypto do you want to sell?")
    time.sleep(1)

    f_btc = open(saves_path_main + "bitcoin.txt", 'r+')
    btc_owned = f_btc.read()
    f_btc.close()

    f_eth = open(saves_path_main + "ethereum.txt", 'r+')
    eth_owned = f_eth.read()
    f_eth.close()

    f_binance = open(saves_path_main + "binance.txt", 'r+')
    binance_owned = f_binance.read()

    f_tether = open(saves_path_main + "tether.txt", 'r+')
    tether_owned = f_tether.read()

    print("1. Bitcoin:")
    print("Owned: " + btc_owned + "\n")

    print("2. Ethereum:")
    print("Owned: " + eth_owned + "\n")

    print("3. Binance Coin:")
    print("Owned: " + binance_owned + "\n")

    print("4. Tether:")
    print("Owned: " + tether_owned + "\n")

    sell_choice = input(": ")
    selling_name = ""
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
    print("How much to sell of crypto?")
    sell_amount = str2float(input(": "))

    # Removing Crypto from Account

    selling = float(selling) - float(sell_amount)
    if float(selling) < 0:
        print("Not enough Crypto!")
        selling = float(selling) + float(sell_amount)

    elif float(selling) >= 0:
        time.sleep(1)
        input("Press ENTER to confirm sell...")
        f_confirm_sell_save = open(save_file_sell, 'w')
        f_confirm_sell_save.write(str(selling))
        f_confirm_sell_save.close()
        # close the fucking files XD
        price_current_sell = 0.0
        if sell_choice == "1":
            price_current_sell = crypto.bitcoin_price()
        elif sell_choice == "2":
            price_current_sell = crypto.ethereum_price()
        elif sell_choice == "3":
            price_current_sell = crypto.binance_owned()
        elif sell_choice == "4":
            price_current_sell = crypto.tether_price()
          

        money_adding_sell = price_current_sell * sell_amount

        f_money_sell = open(saves_path_main + "money.txt", 'r')
        money_sell_bank = str2float(f_money_sell.read())
        f_money_sell.close()

        f_money_sell = open(saves_path_main + "money.txt", "w")
        f_money_sell.write(str(money_sell_bank + money_adding_sell))
        f_money_sell.close()
        
        print("You got: $" + str(money_adding_sell + money_sell_bank) +
              "\n" + "from selling: " + str(sell_amount) + " " + selling_name)


def main_menu():
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
        show_cypto()
        input("Press enter to exit...")
    
    if menu_choice == "2":
        sell_crypto()
        input("Press enter to exit...")
    
    if menu_choice == "3":
        print("Work in progress")

    if menu_choice == "4":
        print("Work in progress")

    if menu_choice == "5":
        print("Exiting...")
        time.sleep(3)
        exit()


if os.path.isfile(saves_path_main + "tutorial.txt"):
    main_menu()
else:
    tutorial()
