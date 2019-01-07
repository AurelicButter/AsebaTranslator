from sys import exit
from json import loads
from lib.fileGenerate import generate

def init():
    fileLocation = input("Enter file location: ")

    if (fileLocation.startswith("C:") != True): #Easier if it's in root folder
        fileLocation = "./" + fileLocation

    try: #Verifies the file location, if doesn't exist, exit with a message.
        open(fileLocation, "r")
    except FileNotFoundError:
        exit("Error: " + fileLocation + " is not found.") #File not found

    data = loads(open(fileLocation).read()) #JSON data

    option = check(data) #Checks the file for anything missing

    AESLPATH = fileLocation[0:-4] + "aesl" #AESL file path
    generate(open(AESLPATH, "w"), data, option) #Initializes and translates the AESL file

def check(data):
    options = { "constants": True, "variables": True, "events": True, "statements": True, "subs": True }

    try:
        data["constants"]
    except:
        options["constants"] = False

    try:
        data["variables"]
    except:
        options["variables"] = False

    try:
        data["events"]
    except:
        options["events"] = False

    try:
        data["subs"]
    except:
        options["subs"] = False

    try:
        data["statements"]
    except:
        print("Error: The statements are missing from JSON file")
        exit()

    return options
