class initFile(object):
    def __init__(self, fileStream):
        #Assigns the filestream to the class
        self.fileStream = fileStream
    def emptyLine(self, amount):
        #Adds an empty line based on the amount
        for x in range(amount):
            self.fileStream.write("\n")    
    def writeln(self, item):
        #Writes a line of a file and moves to a new line
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
            elif (type(items[key]) != list and items[key].startswith("nullArray")): #Creates an empty array essentially. All values are 0
                initArray = [0] * int(float(items[key][10:-1]))
                value1 = "%s[%d]" % (key, len(initArray))
                value2 = "= {}".format(initArray)
            else:
                value2 = "= {}".format(items[key])
            self.writeln("var {} {}".format(value1, value2))
    def events(self, items): #Sets up events
        for key in items:
            data = items[key]
            self.writeln("onevent {}".format(key.replace("_", ".")))

            for event in data: #Checks for what is needed of the event
                if ("condition" in data[event]): #If statements
                    self.writeln("\tif {} {} then".format(event, data[event].get("condition").replace("equals", "==").replace("greater than", ">")))
                    if (isinstance(data[event].get("action"), dict)): #Multiple actions check
                        for x in range(len(data[event]) - 1):
                            statements = data[event].get("action")
                            for state in statements:
                                self.writeln("\t\t{} {}".format(state, statements[state].get("action").replace("equals", "=")))
                    else:
                        self.writeln("\t\t{}".format(data[event].get("action")))   
                    self.writeln("\tend")
                elif (isinstance(data[event], list)): #Regular command calls
                    self.writeln("\tcall {}".format(data[event][0]))
                else: #No conditional, just all actions
                    for x in range(len(data[event])):
                        self.writeln("\t{} {}".format(event, data[event].get("action").replace("equals", "=")))  
    def statements(self, items):
        for x in range(len(items)):
            self.writeln("{}".format(items[x].replace("equals", "=")))          
    def setUp(self, file):
        self.file = file
        #Sets up basic AESL file for translation
        self.writeln("<!DOCTYPE aesl-source>\n<network>\n")
        self.writeln("<!--list of global events-->")
        self.emptyLine(2)
        self.constants(file["constants"])
        self.writeln("<!--show keywords state-->")
        self.writeln('<keywords flag="true"/>')
        self.emptyLine(2)
        self.variables(file["variables"])
        self.events(file["events"])
        self.statements(file["statements"])
        self.writeln("</node>\n\n</network>")