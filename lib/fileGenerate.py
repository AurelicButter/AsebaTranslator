from lib.changeString import change

class initFile(object):
    def __init__(self, fileStream): #Assigns the filestream to the class
        self.fileStream = fileStream
    def writeln(self, item): #Writes a line of a file and moves to a new line
        self.fileStream.write(item + "\n")
    def constants(self, items): #Writes constants to the AESL file
        self.writeln("<!--list of constants-->")
        for key in items:
            self.writeln('<constant value="{}" name="{}"/>'.format(items[key], key))
        self.writeln("\n")
    def variables(self, items): #Writes all variables to the AESL file. Will be located on the top.
        self.fileStream.write('<!--node thymio-II-->\n<node nodeId="1" name="thymio-II">')
        for key in items:
            if (type(items[key]) == list): #Sets up the array name
                value1 = "%s[%d]" % (key, len(items[key]))
            else:
                value1 = key
            
            if (items[key] == None): #Null values. Variables won't have an assigned value
                value2 = ""
            elif (type(items[key]) != list and type(items[key]) != int):
                if (items[key].startswith("fillArray")): #Fills an array with a value
                    value3 = items[key][10:-1].split("][") #Turns the two numbers into their own values
                    initArray = [int(float(value3[1]))] * int(float(value3[0]))
                    value1 = ("%s[%d]" % (key, len(initArray)))
                    value2 = "= {}".format(initArray)
                elif (items[key].startswith("nullArray")): #Creates an empty array essentially. All values are 0
                    initArray = [0] * int(float(items[key][10:-1]))
                    value1 = "%s[%d]" % (key, len(initArray))
                    value2 = "= {}".format(initArray)
            else:
                value1 = value1 + " = {}".format(items[key])
                value2 = ""
            self.writeln("var {} {}".format(value1, value2))
    def events(self, items): #Sets up events
        for key in items:
            data = items[key]
            self.writeln("onevent {}".format(key.replace("_", ".")))

            for event in data: #Checks for what is needed of the event
                if ("condition" in data[event]): #If statements
                    self.writeln("\tif {} {} then".format(event, change(data[event].get("condition"), True)))
                    if (isinstance(data[event].get("action"), dict)): #Multiple actions check
                        for x in range(len(data[event]) - 1):
                            statements = data[event].get("action")
                            for state in statements:
                                self.writeln("\t\t{} {}".format(state, change(statements[state].get("action"), False)))
                    else:
                        self.writeln("\t\t{}".format(data[event].get("action")))   
                    self.writeln("\tend")
                elif (isinstance(data[event], list)): #Regular command calls
                    self.writeln("\tcall {}".format(data[event][0]))
                else: #No conditional, just all actions
                    for x in range(len(data[event])):
                        self.writeln("\t{} {}".format(event, change(data[event].get("action"), False))) 
    def statements(self, items):
        for x in range(len(items)):
            self.writeln("{}".format(change(items[x], False)))          
    def setUp(self, file, AESLPATH):
        self.writeln("<!DOCTYPE aesl-source>\n<network>\n") #Sets up basic AESL file for translation
        self.writeln("\n<!--list of global events-->")
        self.writeln("\n")
        self.constants(file["constants"]) #Sets up all constants
        self.writeln("<!--show keywords state-->")
        self.writeln('<keywords flag="true"/>')
        self.writeln("\n")
        self.variables(file["variables"]) #Sets up all variables
        self.events(file["events"]) #Sets up all events
        self.statements(file["statements"]) #Sets up all statements
        self.writeln("</node>\n")
        self.writeln("\n</network>")
        print("File translation completed.")
