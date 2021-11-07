import mod_bootloader
import time


def main_menu():
    print("Cryptillionaire Mod Bootloader Config:")
    time.sleep(1)
    print("1. Flush mod_storage")
    print("2. Start Init")
    print("3. Register Mods")
    selection = input(": ")
    if int(selection) == 1:
        mod_bootloader.flush_mod_storage()
    elif int(selection) == 2:
        mod_bootloader.init()
    elif int(selection) == 3:
        mod_bootloader.register_mods()
    else:
        print("This is not a valid Input!")

main_menu()