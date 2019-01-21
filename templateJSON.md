# How to Format JSON Files
> "JSON (JavaScript Object Notation) is a lightweight data-interchange format" - https://www.json.org

There are five objects inside the JSON file for translation: constants, variables, events, statements, and subs (short for subroutines). Your JSON file must contain statements in order for the translator to translate the file. All others are optional.

# Constants
```JSON
"constants": {
    "NAME": 0
} 
```
Constants are self-explanatory. The `"NAME"` value is the name while the value is the constant's value. **All values must be an integer**. Otherwise, the translator will refuse to translate the file.


# Variables
```JSON
"variables": {
    "NAME": "value"
}
```
Unlike constants, variables can contain arrays and even contain no value.

__Null values__
```Javascript
"NAME": null
```
> No need to document was a null value does, given that users are required to code in Aseba for the Thymio II robots.

__Arrays__
```Javascript
"arr": [500, 600, 700, 800, 900, 1000, 2000, 5000, 10000, 15000],
"nullArray": "nullArray[10]",
"fillArray": "fillArray[10][254]"
```

There are three ways a user can get an array value. 

The first is the traditional method of inputting all the values like any other array.

Next, the user can use "nullArray". A nullArray is a keyword used to fill an array with x amount of zeros. Input `"nullArray[x]"`, x being the number of values. 

Lastly, the user can use "fillArray". Much like the nullArray, the user can fill an array with x amount of values but instead of zeroes, the user can assign what value is put in. Input `"fillArray[x][y]"`, x being the number of values and y being the value to fill with.

Example: [Arrays.json](examples/Arrays.json)


# Events
```JSON
"events": {
    "NAME": {
        "name": {
            "condition": "STATEMENT",
            "action": "ACTION"
        },
        "Name": [
            "STATEMENT",
            "STATEMENT"
        ],
        "otherN": "ACTION"
    },
    "EVENT NAME": [
        "STATEMENT",
        "STATEMENT"
    ]
}
```

Each event is represented by the "EVENT NAME" value. **This is only for Thymio II pre-programmed events.** If the user wants to make their own function, they must go to the [subs section](#subs).

The event's value can either be a list or an object. If the event value is an object, the user is open to if statements. If plain statements are needed in the object, the user can provide a name value that starts with "other". 

__If Statements__
```JSON
"ACTION NAME": {
    "condition": "STATEMENT",
    "action": "STATEMENT"
},

"ACTION NAME": {
    "condition": "STATEMENT",
    "action": [
        "STATEMENT",
        "STATEMENT"
    ]
}
```
There are two ways to do an if statement in an event. Both need to be an object with two values, "condition" and "action". The action value can also be a string (for one line) or a list (for multiple lines). 

An action can also contain inside if statements as well. See [doubleIf.json](examples/doubleIf.json).

Example: [Events.json](examples/Events.json)

# Statements
```JSON
"statements": [ 
    "STATEMENT",
    "STATEMENT"
]
```

Statements are always a list of strings. Each string represents one line of Aseba code. The user must type everything as there is no support for nullArrays, fillArrays, etc... 

# Subs
```JSON
"subs": {
    "event NAME": [
        "STATEMENT",
        "STATEMENT"
    ]
}
```
Subs (subroutines) perform exactly like events, except for the name of the sub. The user can name the sub whatever they like as long as it is not a keyword for Aseba. See [Events](#events) for formatting information.