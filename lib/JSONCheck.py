#Checks if all values are in the JSON file.s
def JSONCheck(data):
    check = False
    try:
        data["constants"]
    except:
        JSONQuit("Constants")
        check = True

    try:
        data["variables"]
    except:
        JSONQuit("Variables")
        check = True

    try:
        data["events"]
    except:
        JSONQuit("Events")
        check = True

    try:
        data["statements"]
    except:
        JSONQuit("Statements")
        check = True

    return check    

def JSONQuit(location):
    print("Error: {} is missing from JSON file".format(location))
