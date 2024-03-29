#Goes through and changes most mathimatical keywords (ie: greater than, not equal to)
#Includes a variable for if the text is for a conditional for "==" instead of "="

def change(text, condition):
    text = text.replace("greater than or equals", ">=").replace("less than or equals", "&lt;=")
    text = text.replace("greater than", ">").replace("less than", "&lt;")
    text = text.replace("not equal to", "!=")

    #Basic math symbol check
    text = text.replace("minus", "-").replace("plus", "+").replace("multiply by", "*").replace("divided by", "/")

    if (condition == True):
        text = text.replace("equals", "==")
    else:
        text = text.replace("equals", "=")
    return text