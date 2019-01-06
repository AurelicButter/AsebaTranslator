import lib.formating
from lib.changeString import change

class initFile(object):
    def __init__(self, fileStream): #Assigns the filestream to the class
        self.fileStream = fileStream
    #def subs(self, items) #Sets up the subroutines   
    def setUp(self, file, AESLPATH, options):
        genLib = lib.formating #Shorter name for better reading
        #Sets up basic AESL file for translation
        self.fileStream.write("<!DOCTYPE aesl-source>\n<network>\n\n\n<!--list of global events-->\n\n\n")

        if (options["constants"] == True): #Sets up the constants
            self.fileStream.write(genLib.constant(file["constants"]))
        else:
            self.fileStream.write(genLib.constant({}))

        self.fileStream.write('<!--show keywords state-->\n<keywords flag="true"/>\n\n\n') #Spaced out in case of keyword manipulation
        self.fileStream.write('<!--node thymio-II-->\n<node nodeId="1" name="thymio-II">')

        if (options["variables"] == True): #Sets up the variables
            self.fileStream.write(genLib.variable(file["variables"]))

        if (options["events"] == True): #Sets up the events
            self.fileStream.write(genLib.event(file["events"]))

        for x in range(len(file["statements"])): #Sets up all statements
            self.fileStream.write("{}\n".format(change(file["statements"][x], False))) 

        self.fileStream.write("</node>\n\n\n</network>")

        print("File translation completed.\nPress any key to exit...\n")
        input()
