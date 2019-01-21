from lib.changeString import change

def ifState(key, data):
    statement = "\tif {} {} then\n".format(key, change(data.get("condition"), True))

    action = data.get("action")
    if (type(action) == list):
        for x in range(len(action)):
            statement = statement + "\t\t" + change(action[x], False) + "\n"
        return statement + "\tend\n"
    elif (type(action) == str):
        return statement + "\t\t" + change(action, False) + "\n\tend\n"
    else:
        return False

def constant(items): #Generates the constants part of the AESL file
    text = "<!--list of constants-->\n"
    for key in items:
        if (type(items[key]) == int):
            text = text + '<constant value="{}" name="{}"/>\n'.format(items[key], key)
        else:
            return
    return text + "\n"

def variable(items): #Generates the variable part of the AESL file.
    text = ""
    for key in items:
        if (type(items[key]) == list): #Sets up the array name
            value = "%s[%d]" % (key, len(items[key]))
        else:
            value = key

        if (items[key] != None): #None values don't need any more addition items added to the value variable.
            if (type(items[key]) != list and type(items[key]) != int):
                if (items[key].startswith("fillArray")): #Fills an array with a value
                    value3 = items[key][10:-1].split("][") #Turns the two numbers into their own values
                    initArray = [int(float(value3[1]))] * int(float(value3[0]))
                    value= ("%s[%d]" % (key, len(initArray))) +  " = {}".format(initArray)
                elif (items[key].startswith("nullArray")): #Creates an empty array essentially. All values are 0
                    initArray = [0] * int(float(items[key][10:-1]))
                    value = "%s[%d]" % (key, len(initArray)) + " = {}".format(initArray)
            else:
                value += " = {}".format(items[key])

        text = text + "var {}\n".format(value)
    return text

def event(items):
    text = ""
    for key in items:
        data = items[key]
        text = text + "onevent {}\n".format(key)
        if (type(data) == dict):
            for event in data: #Checks for what is needed of the event
                if (type(data[event]) == dict): #If statements
                    item = ifState(event, data[event])

                    if (item == False):
                        return
                    else:
                        text = text + item
                elif (type(data[event]) == list): #List of statements
                    for x in range(len(data[event])):
                        if (type(data[event][x]) == dict):
                            item = ifState(event, data[event][x]) 

                            if (item == False):
                                return
                            else:
                                text = text + item
                        elif (type(data[event][x]) == str):
                            text = text + "\t" + change(data[event][x], False) + "\n"
                        else:
                            return
                elif (type(data[event]) == str): #Variable value change or plain statement
                    if (event.startswith("other")): #Plain statement
                        text = text + "\t" + change(data[event], False) + "\n"
                    else: #Variable change
                        text = text + "\t{} {}\n".format(key, change(data[event], False))
                else: 
                    return
        elif (type(data) == list):
            for x in range(len(data)):
                text = text + "\t{}\n".format(change(data[x], False))
        else:
            text = text + "\t{}\n".format(change(data, False))
    return text

def sub(items):
    text = ""
    for eventName in items:
        for key in items[eventName]:
            data = items[eventName][key]
            text = text + "sub " + key + "\n"

            if (type(data) == dict): #If statements
                item = ifState(key, data)

                if (item == False):
                    return
                else:
                    text = text + item
            elif (type(data) == list): #Plain statements
                for x in range(len(data)):
                    text = text + "\t" + change(data[x], False) + "\n"
            elif (type(data) == str): #Variable value change
                text = text + "\t{} {}\n".format(key, change(data, False))
            else: 
                return
    return text