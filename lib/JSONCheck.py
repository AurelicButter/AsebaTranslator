#Checks if all values are in the JSON file.
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
        
    try:
        data["subs"]
    except:
        JSONQuit("Subs")
        check = False

    return check    

def JSONQuit(location):
    print("Error: {} is missing from JSON file".format(location))
