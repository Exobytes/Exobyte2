"""
This will load all the functions of Exobyte
"""
from libraries.temp import sys as sysC
import network.main as network


def core_menu():

    print("[1] Networking")
    print("[2] CommandLine")
    print("[3] Settings")
    print("[4] Quit")

    while True:
        commandscol = ">>>: "
        commands = input(commandscol)
        if commands == "1":
            print("You typed 1")
            network.network_main()
            return False
        elif commands == "2":
            print("You typed 2")
            # load class
            return False
        # goes to map/class directory
        elif commands == "3":
            print("You typed 3")
            # load class
            return False
        # goes to map/class directory
        elif commands == "4":
            print("Are you sure? Yes/no")
            commands = input(">>>: ")
            if commands == "No" or "no":
                core_menu()
            elif commands == "Yes" or "yes":
                sysC.exit(Quit)
        else:
            print("Not valid!")

core_menu()