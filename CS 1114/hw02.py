def printTwoCharacters():
    '''This function prints two characters a certain number of times depending on the distance between them in the alphabet'''
    firstChar = str(raw_input("Enter a letter: "))
    secondChar = str(raw_input("Enter another letter: "))
    
    firstOrd = ord(firstChar)
    secondOrd = ord(secondChar)

    multiplier = abs(firstOrd - secondOrd)

    print((firstChar + secondChar) * (multiplier))
