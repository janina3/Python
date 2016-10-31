#!/usr/bin/python

'''
Programmer: Janina Soriano
Username: js7187

This program plays the hit and miss game infinitely, unless there is a malfunction with the computer.

Constraints: None

Assumptions: None

'''

import random

def playOneHitAndMatchGame():
    '''the hit and match game that the user can play once'''
    welcome()
    (left, middle, right) = chooseHouseDigits()
    (userL, userM, userR, digitType) = userChooseDigits()
    (invalidTry) = checksThreeDigits(userL, userM, userR, digitType)
    if (invalidTry == "True"):
        return
    else:
        (invalidTry) = checksTwoDigits(userL, userM, digitType)
        if (invalidTry == "True"):
            return
        else:
            (invalidTry) = checksTwoDigits(userL, userR, digitType)
            if (invalidTry == "True"):
                return
            else:
                (invalidTry) = checksTwoDigits(userM, userR, digitType)
                if (invalidTry == "True"):
                        return
                else:
                    (hits, matches) = numHitsAndMatches(left, right, middle, userL, userM, userR)
                    showResults(hits, matches)

def welcome():
    print('''
            Welcome to the Hit && Match Game
            Hit any key to start playing...
          ''')
    raw_input()
       
def chooseHouseDigits():
    '''This function randomly chooses three house' digits. No two digits are the same.'''
    left = random.randint(1, 9)
    middle = random.randint(1, 9)
    right = random.randint(1, 9)
    digitType = "house"
    checksThreeDigits(left, middle, right, digitType)
    checksTwoDigits(left, middle, digitType)
    checksTwoDigits(left, right, digitType)
    checksTwoDigits(middle, right, digitType)
    return (left, middle, right)

def checksThreeDigits(digitOne, digitTwo, digitThree, digitType):
    '''This function checks if all three digits are the same'''
    if (digitOne == digitTwo == digitThree):
        if(digitType == "house"):
            print("The game has malfunctioned. Error -77777")
            exit()
        else:
            print("Invalid try")
            invalidTry = "True"
            return invalidTry
    
def checksTwoDigits (digitOne, digitTwo, digitType):
    '''This function checks if any pair of digits is the same'''
    if (digitOne == digitTwo):
        if(digitType == "house"):
            print("The game has malfunctioned. Error -77777")
            exit()
        else:
            print("Invalid try")
            invalidTry = "True"
            return invalidTry

def userChooseDigits():
    '''This function asks the user to guess three different digits.'''
    userL = int(raw_input("Guess a digit for the left between 1 and 9: "))
    userM = int(raw_input("Guess a digit for the middle between 1 and 9: "))
    userR = int(raw_input("Guess a digit for the right between 1 and 9: "))
    digitType = "user"
    return (userL, userM, userR, digitType)

def numHitsAndMatches(left, middle, right, userL, userM, userR):
    '''This function determines and returns the number of hits and matches.'''
    hits = 0
    matches = 0
    if (left == userL):
        hits = 1 + hits
    elif (left == userM or left == userL):
        matches = 1 + matches
        
    if (middle == userM):
        hits = 1 + hits
    elif (middle == userL or middle == userR):
        matches = 1 + matches
        
    if (right == userR):
        hits = 1 + hits
    elif (right == userL or right == userM):
        matches = 1 + matches
    return (hits, matches)

def showResults(hits, matches):
    '''This function shows how many hits and matches the user had.'''
    if (hits == 1):
        print("1 hit")
    else:
        print("%i hits" % hits)
    if (matches == 1):
        print("1 match")
    else:
        print("%i matches" % matches)
    print("Come back and play again sometime")

def main():
    while True:
        playOneHitAndMatchGame()

if __name__ == '__main__':
    main()
