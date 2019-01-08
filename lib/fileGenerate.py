import lib.formating
from lib.changeString import change

def generate(fileStream, file, options):
    genLib = lib.formating #Shorter name for better reading
    #Sets up basic AESL file for translation
    fileStream.write("<!DOCTYPE aesl-source>\n<network>\n\n\n<!--list of global events-->\n\n\n")

    if (options["constants"] == True): #Sets up the constants
        fileStream.write(genLib.constant(file["constants"]))
    else:
        fileStream.write(genLib.constant({}))

    fileStream.write('<!--show keywords state-->\n<keywords flag="true"/>\n\n\n') #Spaced out in case of keyword manipulation
    fileStream.write('<!--node thymio-II-->\n<node nodeId="1" name="thymio-II">')

    if (options["variables"] == True): #Sets up the variables
        fileStream.write(genLib.variable(file["variables"]))

    if (options["subs"] == True): #Sets up the subroutines
        fileStream.write(genLib.sub(file["subs"]))

    if (options["events"] == True): #Sets up the events
        fileStream.write(genLib.event(file["events"]))

    for x in range(len(file["statements"])): #Sets up all statements
        fileStream.write("{}\n".format(change(file["statements"][x], False))) 

    fileStream.write("</node>\n\n\n</network>")

    print("\nFile translation completed.\n")