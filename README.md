# AsebaTranslator
Translates scripted JSON files into Aseba

## Introduction
While in a robotics lab, I could barely manage to work with the Aseba language. So, how do you change that? Make a tool so I can write it in a scripted JSON file and translate it. Simple, easy, and painless, for the most part. This is a tool to help myself create programs for a Thymio II robot for the class.

It takes scripted JSON files and works on creating some simple yet complex programs. It can generate events, constants, and variables with no trouble. However, statements can be a bit tricky in theory if they need to go someplace other than after the events.

## How to use
### Using the EXE program:
Simply load up the program and enter in the file location of the JSON. If the file is in the same root folder, users may provide just the name of the JSON file instead of the entire path. The file location is simply a terminal and will respond like a terminal would for file locations. The AESL file will be placed in the same location as the JSON file for an efficient way of finding it.

### Using the base code:
Requirements:
- Python 3.6.5+

To run the program, simply run `python index.py` in the root folder. From there, see "Using the EXE program".

## License
This is a free to use program licensed under the [MIT license](LICENSE). The program will not be regularly maintained. However, if you feel an improvement would be beneficial, feel free to fork it, update it, and submit a pull request. Better tools make better programs after all.

