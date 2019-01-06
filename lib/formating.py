from lib.changeString import change

def constant(items): #Generates the constants part of the AESL file
    text = "<!--list of constants-->\n"
    for key in items:
        text = text + '<constant value="{}" name"{}"/>\n'.format(items[key], key)
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
            if (type(data[event]) == list):
                if (type(data[event][0]) == dict): #If statements
                    item = data[event]
                    for x in range(len(item)):
                        text = text + "\tif {} {} then\n".format(event, change(item[x].get("condition"), True))
                        if (type(item[x].get("action")) == dict): #Multiple actions for the condition.
                            for y in item[x].get("action"):
                                text = text + "\t\t{} {}\n".format(y, change(item[x].get("action")[y].get("action"), False))
                        else:
                            text = text + "\t\t{}\n".format(item[x].get("action"))  #Just one action for the condition.
                        text = text + "\tend"
                elif (type(data[event][0]) == str): #Other random statements within the event. 
                    for x in range(len(data[event])):
                        text = text + "\t{}\n".format(data[event][x])
            else: #No conditional, just all actions
                for x in range(len(data[event])):
                    text = text + "\t{} {}\n".format(event, change(data[event].get("action"), False))
    return text

def sub(items):
    text = ""
    return text