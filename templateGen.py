#Generates a blank JSON file for a new ASEL file translate.

def menuLanding():
    fName = input("What should the file be called? ")
    JSONTemplate = { "constants": { }, "variables": { }, "events": { }, "statements": [ ], "subs": { } }
    JSONFile = open(fName + ".json", "w")

    JSONFile.write(str(JSONTemplate).replace("'", '"'))
    return