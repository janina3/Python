#!/usr/bin/python

'''
Programmer: Janina Soriano
Username: js7187

This program 

Constraints: None

Assumptions: None

'''

from __future__ import print_function
import random

def getNumStars():
    '''Asks the user for a number of stars'''
    numStars = int(raw_input("How many stars would you like to draw? "))
    while(numStars < 0):
           numStars = int(raw_input("How many stars would you like to draw? "))
        
    return numStars

def drawStar(numStars):
    '''draws a star on the screen'''
    for i in range(numStars):
        print("*", end = '')

def powerList(startVal, endVal, exponent = 2):
    '''Returns the power list'''
    return([i**exponent for i in range(startVal, endVal)])
        

def getPowerList():
    '''Gets the power list from the user'''
    startVal = int(raw_input("Enter a starting value: "))
    endVal = int(raw_input("Enter an ending value: "))
    exponent = int(raw_input("Enter a number for the exponent: "))
    return(startVal, endVal, exponent)

def printHistogram(histList):
    '''Prints a histogram based on the list passed in'''
    for i in histList:
        for j in range(i):
            print("-", end = '')
        print(i)

def main():
    (numStars) = getNumStars()
    drawStar(numStars)
    print()
    (startVal, endVal, exponent) = getPowerList()
    (histList) = powerList(startVal, endVal, exponent)
    printHistogram(histList)
    

if __name__ == '__main__':
    main()
    
