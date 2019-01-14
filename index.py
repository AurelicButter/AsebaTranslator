from sys import exit
from lib.translate import init

def menu():
    print("####### AsebaTranslator v1.0 #######\n")
    print("Enter the number next to the option you would like.")
    print("1. Generate a template file")
    print("2. Translate a JSON file")
    print("0. Exit the program.\n")

    option = int(input())

    if(option == 1): #Generates a blank JSON file for a new ASEL file translate.
        fName = input("What should the file be called? ")
        JSONTemplate = { "constants": { }, "variables": { }, "events": { }, "statements": [ ], "subs": { } }
        JSONFile = open(fName + ".json", "w")

        JSONFile.write(str(JSONTemplate).replace("'", '"'))
        JSONFile.close()
        print("\n" + fName + ".json has been successfully created.\n")
    elif(option == 2):
        init()
    elif(option == 0):
        exit()
    else:
        print("Option not found. Redirecting to the menu...\n")
        
    menu()

menu()