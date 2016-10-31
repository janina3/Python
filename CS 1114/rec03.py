WELCOME_STRING = "Hi there!"
GOODBYE_STRING = "'Bye for now!"

def printWelcome():
    '''prints WELCOME_STRING to user'''
    print (WELCOME_STRING)

def printGoodbye():
    '''prints GOODBYE_STRING to user'''

def printNameInBox(boxChar, fillChar, name):
    '''prints box that fits name, height of 5, with name in box using boxChar and filling with fillChar'''
    length = len(name) + 4
    printRowOfChars(boxChar, length)
    printRowWithFiller(boxChar, fillChar, length)
    printRowWithName(boxChar, fillChar, name)
    printRowWithFiller(boxChar, fillChar, length)
    printRowOfChars(boxChar, length)

def printRowOfChars(char, lengthOfLine):
    '''prints row of size lenghtOfLine ox chars'''
    print (char * lengthOfLine)

def printRowWithFiller(endChar, fillChar, length):
    '''prints row with endChar at either end, fillChars in inbetween. Length of row is denoted by parameter length'''
    print (endChar + (fillChar * (length(-2)) + endChar)

def printRowWithName(endChar, fillChar, name):
    '''prints row with name, bordered on each side by one fillChar and one endChar'''
    print(endChar + fillChar + name + fillChar + endChar)

def main():
    printWelcome()
    printNameInBox()
    printGoodbye()

