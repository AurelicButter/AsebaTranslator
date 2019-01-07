from sys import exit
from templateGen import menuLanding
from lib.translate import init

def menu():
    print("####### AsebaTranslator v1.0 #######\n")
    print("Enter the number next to the option you would like.")
    print("1. Generate a template file")
    print("2. Translate a JSON file")
    print("0. Exit the program.")
    print()

    option = int(input())

    if(option == 1):
        menuLanding()
    elif(option == 2):
        init()
    elif(option == 0):
        exit()
    else:
        print("Option not found. Redirecting to the menu...\n")
        menu()

menu()