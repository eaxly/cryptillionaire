import time
# import sys
import os
# from typing import Counter
import crypto
from datetime import datetime
# rich libaries
from rich import print
from rich.console import Console
import mod_bootloader

mods_installed = mod_bootloader.handshake()
main_run_path = os.path.dirname(os.path.abspath(__file__))


console = Console()


# if this is showing a warning, ignore it, this is a pylance/vscode issue
# the program runs fine! \__(· _ · )__/*
from str2float import str2float
import filer


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
        mod_bootloader.register_mods()
        print("Please Restart your Game to let it finish setting up")


def show_crypto():
    count = 0
    while mods_installed > count:
        print(mod_bootloader.dictionary_names(count))

        print(crypto.price(count))
        count = count + 1


def sell_crypto():
    count2 = 0
    crypto_owned = ""
    p_file=""
    print("What Crypto do you want to sell?")
    while mods_installed > count2:
        crypto_name = str(mod_bootloader.dictionary_names(count2))
        p_file = saves_path_main + crypto_name.lower()
        p_file = p_file.replace("\n", "")

        if filer.filing(p_file):
            crypto_owned = filer.read_file(p_file)
        elif filer.filing(p_file, create_file=True):
            content_placeholder = open(p_file, "w")
            content_placeholder.write("0")
            content_placeholder.close()
            crypto_owned = filer.read_file(p_file)

        print(f"{count2}. {mod_bootloader.dictionary_names(count2)}")
        print(f"Owned: [underline]{crypto_owned}[/]\n")
        count2 = count2 + 1

    sell_choice = input(": ")
    selling_name = ""
    selling = ""
    save_file_sell = ""

    if mods_installed > int(sell_choice):
        selling_name = mod_bootloader.dictionary_names(int(sell_choice))
        selling_name = str(selling_name).replace("\n", "")
        save_file_sell = saves_path_main + str(selling_name).lower()
        save_file_sell = save_file_sell.replace("\n", "")
        selling = crypto_owned = filer.read_file(p_file)

    else:
        print("Invalid Input! Exiting to main menu!")
        time.sleep(5)
        main_menu()


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
        price_current_sell = crypto.price(int(sell_choice))
        price_current_sell = price_current_sell.replace("$", "")
        price_current_sell = price_current_sell.replace(",", "")

        money_adding_sell = float(price_current_sell) * sell_amount

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
    count3 = 0
    crypto_owned = ""
    p_file=""
    print("What Crypto do you want to sell?")
    while mods_installed > count3:
        crypto_name = str(mod_bootloader.dictionary_names(count3))
        p_file = saves_path_main + crypto_name.lower()
        p_file = p_file.replace("\n", "")

        print(f"{count3}. {mod_bootloader.dictionary_names(count3)}")
        print(f"Price: [underline]{crypto.price(count3)}[/]\n")
        count3 = count3 + 1

    if filer.filing(p_file):
        crypto_owned = filer.read_file(p_file)
    elif filer.filing(p_file, create_file=True):
        content_placeholder = open(p_file, "w")
        content_placeholder.write("0")
        content_placeholder.close()
        crypto_owned = filer.read_file(p_file)


    buy_choice = input(": ")

    #Just some declarations
    buying_name = ""
    buying = ""
    save_file_buy = ""

    if mods_installed > int(buy_choice):
        
        buying_name = mod_bootloader.dictionary_names(int(buy_choice))
        buying_name = str(buying_name).replace("\n", "")
        save_file_buy = saves_path_main + str(buying_name).lower()
        save_file_buy = save_file_buy.replace("\n", "")
        buying = crypto_owned = filer.read_file(p_file)

    else:
        print("Invalid Input! Exiting to main menu!")
        time.sleep(5)
        main_menu()


    time.sleep(2)
    print("Selected: " + buying_name + "\n" + "Owned: " + buying)
    print(f"How much {buying_name} to Buy?")
    buy_amount = str2float(input(": "))


    f_money_buy = open(saves_path_main + "money.txt", 'r')
    money_bank = str2float(f_money_buy.read())
    f_money_buy.close()
    price_crypto = 0.0
    price_crypto = crypto.price(int(buy_choice))
    price_crypto = price_crypto.replace("$", "")
    price_crypto = price_crypto.replace(",", "")

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
