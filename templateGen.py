#Generates a blank JSON file for a new ASEL file translate.

def menuLanding():
    fName = input("What should the file be called? ")
    generate(fName)
    return

def generate(fileName):
    JSONTemplate = { "constants": { }, "variables": { }, "events": { }, "statements": [ ], "subs": { } }
    JSONFile = open(fileName + ".json", "w")

    JSONFile.write(str(JSONTemplate).replace("'", '"'))
    return