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

MANAGER_FIRST_NAME = "Manager"
MANAGER_LAST_NAME = "Here"

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

def printMaintainance(count, largest, smallest, sumOfBills, curious):
    '''prints maintainance work'''
    print('''
            Do your maintainance work
            ...and...
            don't forget to restart this program
            '''
            )
    print("Customer count is %i" % count)
    print("Largest bill is $%.2f" % largest)
    print("Smallest bill is $%.2f" % smallest)
    count = float(count)
    average = sumOfBills/count
    print("The average bill is $%.2f" % average)
    curiousPercent = (curious/count) * 100
    print("The percentage of customers who purchased the same number of 32 cent as either of the other stamps is %i" % curiousPercent)
    
def askNumStamps():
    '''asks and returns the number of each stamp the user wants'''
    stamp74 = int(raw_input("How many 74 cent stamps would you like? "))
    stamp32 = int(raw_input("How many 32 cent stamps would you like? "))
    stamp6 = int(raw_input("How many 6 cent stamps would you like? "))
    return(stamp74, stamp32, stamp6)

def getPosNum(stamp, stampCost):
    '''checks if customer is asking for a positive number of stamps and loops while the number is still negative'''
    while (stamp < 0):
        stamp = int(raw_input("Sorry, we do not accept a negative number of stamps. How many %i cent stamps would you like? " % stampCost))
    return stamp
    
def getNewStampNum(stamp74, stamp32, stamp6):
    stampCost = 74
    stamp74 = getPosNum(stamp74, stampCost)
    stampCost = 32
    stamp32 = getPosNum(stamp32, stampCost)
    stampCost = 6
    stamp6 = getPosNum(stamp6, stampCost)
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

def getEnoughBills(dollars, totStampCost):
    '''checks if the customer is giving enough money and loops while there is insufficient funds'''
    while (dollars <= totStampCost):
        missingDollars = totStampCost - dollars
        missingCents = missingDollars - int(missingDollars)
        if (missingCents > 0):
            missingDollars = 1 + missingDollars
        missingDollars = round(missingDollars)
        newDollars = int(raw_input("Insufficient Funds. Must give %i more dollars. How many dollars will you be adding? " % missingDollars))
        dollars = dollars + newDollars
        
def displayWait():
    '''prints the wait message'''
    print("Thank you. Just a moment please...")

def calcChange(totStampCost, dollars):
    '''calculates and returns the amount of change'''
    change = dollars - totStampCost
    return (change)

def thanksForTipAndAdjustsChange(dollars, change):
    '''thanks the user for the excess money stating it is a tip and returns change as the cents amount only'''
    if(change > 1):
        cents = int(change) - change
        tip = change - cents - 1
        print("Thank you for the $%i tip!" % tip)
        change = cents  #not necessary but easier to read
        return change

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

def oneCustomer():
    displayWelcome()
    (firstName, lastName) = askName()
    return(firstName, lastName)

def ifCustomer(firstName):
    (stamp74, stamp32, stamp6) = askNumStamps()
    (stamp74, stamp32, stamp6) = getNewStampNum(stamp74, stamp32, stamp6)
    (numStamps) = calcNumStamps(stamp74, stamp32, stamp6)
    (totStampCost) = stampTotPrice(stamp74, stamp32, stamp6)
    moneyOwed(numStamps, totStampCost)
    dollars = numDollars()
    getEnoughBills(dollars, totStampCost)
    displayWait()
    (change1) = calcChange(totStampCost, dollars)
    (change) = thanksForTipAndAdjustsChange(dollars, change1)
    printNumEachCoins(change1)
    displayThanks()
    displayRatingWelcome(firstName)
    rating = returnRating()
    displayRatingThanks(rating, totStampCost)
    return(totStampCost, stamp6, stamp32, stamp74)
    
def main():
    largest = 0.0
    smallest = 0.0
    count = 0
    sumOfBills = 0.0
    curious = 0
    while True :
        (firstName, lastName) = oneCustomer()
        if (firstName != MANAGER_FIRST_NAME and lastName != MANAGER_LAST_NAME):
            (totalBill, stamp6, stamp32, stamp74) = ifCustomer(firstName)
            if(count == 0):
                count = 1
                smallest = totalBill
                largest = totalBill
                sumOfBills = totalBill
            else:
                if(totalBill > largest):
                    largest = totalBill
                if(totalBill < smallest):
                    smallest = totalBill
                sumOfBills += totalBill
                count += 1
            if(stamp32 == stamp6 or stamp32 == stamp74):
                    curious += 1
                
        else:
            printMaintainance(count, largest, smallest, sumOfBills, curious)
            break
  
if __name__ == '__main__':
    main()
