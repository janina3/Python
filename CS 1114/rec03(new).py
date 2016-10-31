#!/usr/bin/python

'''
Programmer: Janina Soriano

Username: js7817

This program shows the receipt with the welcome, number of coffees, number of donuts, cost of coffees, cost of donuts, cost of tax, total amount owed, and displays goodbye

Constraints: None

Assumptions: None

'''

from __future__ import print_function
import os

COST_OF_COFFEE = 0.77
COST_OF_DONUT = 0.64
TAX_RATE = .0846

def displayWelcome():
    '''prints Hello!'''
    print("Hello!")

def getOrder():
    '''gets the customer's order'''
    numOfCoffees = getNumCoffees()
    numOfDonuts = getNumDonuts()
    return (numOfCoffees, numOfDonuts)

def getNumCoffees():
    '''gets the number of coffees'''
    numOfCoffees = int(raw_input("How many cups of coffee? Please enter an integer: "))
    return numOfCoffees

def getNumDonuts():
    '''gets the number of donuts'''
    numOfDonuts = int(raw_input("How many donuts? Please enter an integer: "))
    return numOfDonuts

def calcAmtOwed(costOfCoffees, costOfDonuts, taxes):
    '''calculates the total amount owed'''
    preTaxAmt = calcPreTaxAmt(costOfCoffees, costOfDonuts)
    taxes = calcTaxes(taxes)
    amtOwed = preTaxAmt + taxes
    return amtOwed

def calcCostOfCoffees(numOfCoffees):
    '''calculates the cost of the coffees'''
    numOfCoffees = getNumCoffees()
    costOfCoffees = numOfCoffees * COST_OF_COFFEE
    return costOfCoffees

def calcCostOfDonuts(numOfDonuts):
    '''calculates the cost of the donuts'''
    numOfDonuts = getNumDonuts()
    costOfDonuts = numOfDonuts * COST_OF_DONUT
    return costOfDonuts

def calcPreTaxAmt(costOfCoffees, costOfDonuts):
    '''calculates the amount before taxes'''
    costOfCoffees = calcCostOfCoffees(costOfCoffees)
    costOfDonuts = calcCostOfDonuts(costOfDonuts)
    preTaxAmt = costOfCoffees + costOfDonuts
    return preTaxAmt
    
def calcTaxes(costOfCoffees, costOfDonuts):
    '''calculates the taxes'''
    preTaxAmt = calcPreTaxAmt(costOfCoffees, costOfDonuts)
    taxes = preTaxAmt * TAX_RATE
    return taxes

def showReceipt():
    '''shows the receipt'''
    printStoreNameAndDesign()
    printBlankLine()
    printCoffeeLine()
    printDonutLine()
    printTaxLine()
    printBlankLine()
    printTotalLine()
    printBlankLine()
    printThanksLine()

def printStoreNameAndDesign():
    '''prints the store name and design'''
    printTopDesign()
    printStoreName()
    printBottomDesign()

def printTopDesign():
    '''prints the top design'''
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")

def printBottomDesign():
    '''prints the bottom design'''
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

def printStoreName():
    '''prints the store name'''
    print("THE COFFEE AND DOUGHNUT SHOPPE")

def printCoffeeLine():
    '''prints the line on the receipt with the number and total cost of the coffees'''
    numOfCoffees = getNumCoffees(numOfCoffees)
    costOfCoffees = calcCostOfCoffees(costOfCoffees)
    print("%i cups of coffee: $%.2f" % (numOfCoffees, costOfCoffees))
          
def printDonutLine():
    '''prints the line on the receipt with the number and total cost of the donuts'''
    numOfCoffees = getNumCoffees(numOfCoffees)
    costOfCoffees = calcCostOfCoffees(costOfCoffees)
    print("%i doughnuts: $%.2f" % (numOfDonuts, costOfDonuts))
          
def printTaxLine(taxes):
    '''prints the line on the receipt with the tax cost'''
    taxes = calcTaxes(taxes)
    print("tax: $%.2f" % (taxes))

def printTotalLine(amtOwed):
    '''prints the line on the receipt with the total amount owed'''
    amtOwed = calcAmtOwed(amtOwed)
    print("Amount Owed: $%.2f" % (amtOwed))

def printThanksLine():
    '''prints Thank you for buying local.'''
    print("Thank you for buying local.")

def printBlankLine():
    '''prints a blank line'''
    print(" ")
          
def main():
    displayWelcome()
    (numOfCoffees, numOfDonuts) = getOrder()
    calcAmtOwed()


if __name__ == "__main__":
    main()


    

