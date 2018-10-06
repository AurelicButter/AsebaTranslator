import sys
import fileGenerate
import json #For initial reading of the JSON file

fileLocation = input("Enter file location: ")

if (fileLocation.startswith("C:") != True): #Easier if it's in root folder
    fileLocation = "./" + fileLocation

try:
    open(fileLocation, "r")
except FileNotFoundError:
    sys.exit("Error: " + fileLocation + " is not found.") #File not found

convertFile = fileGenerate.initFile(open(fileLocation[0:-4] + "aesl", "w"))
convertFile.setUp(json.loads(open(fileLocation).read())) #Init and translate AESL file