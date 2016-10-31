#!/usr/bin/python

'''
Programmer: Janina Soriano
Username: js7187

Constraints: None

Assumptions: None

'''

from moneyChangerNew import quantityOfCoins
from moneyChangerNew import printAsCoins

import random

def displayWelcome():
    '''displays the welcome message inside a box'''
    print('''
    --------------------------------------------
    |     Welcome to the snakeStamp Machine!     |
    | We dispense only 74, 32 and 6 cent stamps. |
    | We give only coins in change - (no bills). |
     --------------------------------------------

     ''')

def askName():
    '''asks and returns the user's first and last name'''
    firstName = str(raw_input("What is your first name? "))
    lastName = str(raw_input("What is your last name? "))
    return (firstName, lastName)

def askNumStamps():
    '''asks and returns the number of each stamp the user wants'''
    stamp74 = int(raw_input("How many 74 cent stamps would you like? "))
    stamp32 = int(raw_input("How many 32 cent stamps would you like? "))
    stamp6 = int(raw_input("How many 6 cent stamps would you like? "))
    return(stamp74, stamp32, stamp6)

def calcNumStamps(stamp74, stamp32, stamp6):
    '''returns the total number of stamps'''
    numStamps = stamp74 + stamp32 + stamp6
    return (numStamps)
    
def stampTotPrice(stamp74, stamp32, stamp6):
    '''returns the total cost of the stamps'''
    cost74 = stamp74 * .74
    cost32 = stamp32 * .32
    cost6 = stamp6 * .06
    totStampCost = cost74 + cost32 + cost6
    return (totStampCost)

def moneyOwed(numStamps, totStampCost):
    '''prints the price of all the stamps'''
    if numStamps == 1:
        print("The price of your 1 stamp is %.2f" % (totStampCost))
    else:
        print("The price of your %i stamps is $%.2f" % (numStamps, totStampCost))
    
def numDollars():
    '''returns the number of dollars the user will be paying with'''
    dollars = int(raw_input("How many dollars will you be giving us? "))
    return (dollars)

def displayWait():
    '''prints the wait message'''
    print("Thank you. Just a moment please...")

def calcChange(totStampCost, dollars):
    '''calculates and returns the amount of change'''
    change = dollars - totStampCost
    return (change)

def printNumEachCoins(change):
    '''prints the number of each coin for change'''
    quantityOfCoins(change)
    printAsCoins(change)

def displayThanks():
    '''displays thank you'''
    print('''

    ---=======================================---
    --- Thank you for using our stamp machine ---
    ---=======================================---

    ''')

def displayRatingWelcome(firstName):
    '''prints the welcome message for the rating'''
    print("CONGRATULATIONS %s!" % firstName)
    print("You have been chosen to help us evaluate our machine.")
    print("For helping us you will have a chance to win a prize.")

def returnRating():
    '''returns the rating the user gave'''
    rating = int(raw_input("Please rate our machine by entering a number between 1 and 10, with 10 being really great and 1 being horrible: "))
    return (rating)

def displayRatingThanks(rating, totStampCost):
    '''returns the goodbye and thank you message for rating'''
    if (random.randint(1, 1000) == rating):
        print("You win $50!")
    elif (rating == 2 or rating == 4 or rating == 7) or ((totStampCost >= 17.25) and (totStampCost <=58.42)):
        print("You win $2.33!!!")
    elif (totStampCost > 1.37):
        print("You win 37 cents!!!")
    else:
        print("You win 3 cents!!!")
    print("Thank you for using our stamp machine.")

def printRandBanner():
    '''prints random banner'''
    printTopDesign()

    printBottomDesign()

def printTopDesign():
    '''prints the top design'''
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")

def printBottomDesign():
    '''prints the bottom design'''
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

def printLine1():
    '''prints the first middle line'''
    lineMultiplier = random.randint(4, 5)
    charMultiplier = random.randint(4, 6)

def printLine2():
    '''prints the second middle line'''

def printLine3():
    '''prints the third middle line'''
    
def main():
    displayWelcome()
    (firstName, lastName) = askName()
    (stamp74, stamp32, stamp6) = askNumStamps()
    (numStamps) = calcNumStamps(stamp74, stamp32, stamp6)
    (totStampCost) = stampTotPrice(stamp74, stamp32, stamp6)
    moneyOwed(numStamps, totStampCost)
    dollars = numDollars()
    displayWait()
    (change) = calcChange(totStampCost, dollars)
    printNumEachCoins(change)
    displayThanks()
    displayRatingWelcome(firstName)
    rating = returnRating()
    displayRatingThanks(rating, totStampCost)
    printRandBanner()
    
if __name__ == '__main__':
    main()
