import lib.formating
from os import remove
from lib.changeString import change

def generate(fileStream, file, options):
    genLib = lib.formating #Shorter name for better reading
    #Sets up basic AESL file for translation
    fileStream.write("<!DOCTYPE aesl-source>\n<network>\n\n\n<!--list of global events-->\n\n\n")

    if (options["constants"] == True): #Sets up the constants
        try:
            fileStream.write(genLib.constant(file["constants"]))
        except:
            return errMsg("constants", fileStream, options["PATH"])
    else:
        fileStream.write(genLib.constant({}) + "\n")

    fileStream.write('<!--show keywords state-->\n<keywords flag="true"/>\n\n\n<!--node thymio-II-->\n<node nodeId="1" name="thymio-II">')

    if (options["variables"] == True): #Sets up the variables
        try:
            fileStream.write(genLib.variable(file["variables"]))
        except:
            return errMsg("variables", fileStream, options["PATH"])

    if (options["subs"] == True): #Sets up the subroutines
        try:
            fileStream.write(genLib.sub(file["subs"]))
        except:
            return errMsg("subs", fileStream, options["PATH"])

    if (options["events"] == True): #Sets up the events
        try:
            fileStream.write(genLib.event(file["events"]))
        except:
            return errMsg("events", fileStream, options["PATH"])

    for x in range(len(file["statements"])): #Sets up all statements
        fileStream.write("{}\n".format(change(file["statements"][x], False))) 

    fileStream.write("</node>\n\n\n</network>")

    print("\nFile translation completed.\n")

def errMsg(itemType, fileStream, PATH):
    print("\nLocation: {} object\nUnknown data type. Please review and try again.\n".format(itemType))
    fileStream.close()
    return remove(PATH)