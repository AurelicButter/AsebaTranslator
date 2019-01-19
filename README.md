# AsebaTranslator
Translates scripted JSON files into Aseba

## Introduction
The AsebaTranslator is a tool made to understand and program in Aseba. It is able to translate user-created/user-edited JSON files into AESL files (The file type for  Aseba) and generate templates for the user to edit and later use in the translator. 

## Aseba Programming Language
Aseba is a programming language used to communicate with a Thymio II robot and relay directions. It's often used in educational settings such as schools as an introduction to robotics and programming.

More information:

[Aseba Github](https://github.com/aseba-community/aseba) | [Thymio II Website (English)](https://www.thymio.org/home-en:home)

***

## Requirements
### EXE Program: 
Windows OS (Recommended: Windows 10)
> There is no support for Linux and MacOS based on the capabilities of the [PyInstaller](http://www.pyinstaller.org) package I use to generate the file. You are welcome to turn it into an EXE file for your system's OS. 

### Source Code: 
Python 3.6.5+
> By using the source code, I will assume you know basic Python skills. There will be no support for it.

## Set Up AsebaTranslator
> This program has only been tested in Aseba Studio. I have no clue if AESL files will work with the Visual or Blocky programming methods provided by the Aseba team.

Both the EXE and source code work in a root folder. Place the program in a folder to work from. While it is easier to input the JSON file's path folder in the program, as long as the translator can find the JSON file, the AESL file will be located in the same place.

### Template Generation:
The AsebaTranslator can generate a blueprint JSON file for the user to edit and work in. Simply input 1 in the menu and then give it a location to generate the JSON file. (See [Path Locations](#path-locations) for file locations)

### Translation and Loading:
For formatting your JSON files, see [templateJSON.md](./templateJSON.md)

Translating a JSON file is made simple. Input 2 in the menu and then give it the JSON file's location. (See [Path Locations](#path-locations) for file locations) Upon successful translation, the AESL file will be in the same place as the JSON file path. Open up Aseba Studio and load the program like you would any other saved file.

#### Path Locations
If the file is in the same folder as the program, simply type the name of the file.
`template` would refer to the `template.json` in the same folder.

If the file is located in a subfolder of the program's, input the folder and file name. Example: `EpicProject\version1` would refer to the `<Location of program>/EpicProject/version1.json` file.

If the file is located somewhere else, input the entire path. Example: `C:\Users\<Username>\Documents\<File Name>`.

***

## License
This is a free to use program licensed under the [MIT license](LICENSE). The program will not be regularly maintained. However, if you feel an improvement would be beneficial, feel free to fork it, update it, and submit a pull request. Better tools make better programs after all.

