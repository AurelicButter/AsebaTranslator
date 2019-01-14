from lib.changeString import change

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
        text = text + "onevent {}\n".format(key.replace("_", "."))
        for event in data: #Checks for what is needed of the event
            if (type(data[event]) == dict): #If statements
                text = text + "\tif {} {} then\n".format(key, change(data[event].get("condition"), True))

                if (type(data[event].get("action")) == list): #Mutliple statements for the if statement
                    for x in data[event].get("action"):
                        text = text + "\t\t" + change(data[event].get("action")[x], False) + "\n"
                elif (type(data[event].get("action")) == str): #Just one statement
                    text = text + "\t\t" + change(data[event].get("action"), False) + "\n"
                else:
                    return

                text = text + "\tend\n"
            elif (type(data[event]) == list): #Plain statements or multiple if statements
                for x in range(len(data[event])):
                    if (type(data[event][x]) == dict):
                        text = text + "\tif " + event + " " + change(data[event][x].get("condition"), True) + " then\n"
                        
                        if (type(data[event][x].get("action")) == list): #Mutliple statements for the if statement
                            for x in range(len(data[event][x].get("action"))):
                                text = text + "\t\t" + change(data[event][x].get("action")[x], False) + "\n"
                        elif (type(data[event][x].get("action")) == str): #Just one statement
                            text = text + "\t\t" + change(data[event][x].get("action"), False) + "\n"
                        else:
                            return

                        text = text + "\tend\n"
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
    return text

def sub(items):
    text = ""
    for eventName in items:
        eventItem = items[eventName]
        for key in eventItem:
            data = eventItem[key]
            text = text + "sub " + key + "\n"

            if (type(data) == dict): #If statements
                text = text + "\tif {} {} then\n".format(key, change(data.get("condition"), True))

                if (type(data.get("action")) == list): #Mutliple statements for the if statement
                    for x in data.get("action"):
                        text = text + "\t\t" + change(data.get("action")[x], False) + "\n"
                elif (type(data.get("action")) == str): #Just one statement
                    text = text + "\t\t" + change(data.get("action"), False) + "\n"
                else:
                    return

                text = text + "\tend\n"
            elif (type(data) == list): #Plain statements
                for x in range(len(data)):
                    text = text + "\t" + change(data[x], False) + "\n"
            elif (type(data) == str): #Variable value change
                text = text + "\t{} {}\n".format(key, change(data, False))
            else: 
                return
    return text