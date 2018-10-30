from sys import exit
from lib.fileGenerate import initFile
from lib.JSONCheck import JSONCheck
import json #For initial reading of the JSON file

fileLocation = input("Enter file location: ")

if (fileLocation.startswith("C:") != True): #Easier if it's in root folder
    fileLocation = "./" + fileLocation

try:
    open(fileLocation, "r")
except FileNotFoundError:
    exit("Error: " + fileLocation + " is not found.") #File not found

data = json.loads(open(fileLocation).read()) #JSON data

result = JSONCheck(data) #Checks for missing JSON values.
if (result == True): #If true, exit program. Error message is printed already.
    exit()

AESLPATH = fileLocation[0:-4] + "aesl" #AESL file path
convertFile = initFile(open(AESLPATH, "w")) #Inits the AESL file
convertFile.setUp(data, AESLPATH) #Translate AESL file