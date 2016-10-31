#!/usr/bin/python/

'''
Programmer: Janina Soriano
Username: js7817

This prints out Welcome, a 7x5 box with 'joe' in the middle, then Thanks

'''

from __future__ import print_function
import os


def drawSevenXs():
    '''draws 7 Xs in a row'''
    print("""XXXXXXX""")
            
def drawTwoXs():
    '''draws a row with an X in the beginning and an X in the end with 5 spaces between'''
    print("""X     X""")

def drawXJoeX():
    '''draws X, space, joe, space X'''
    print("""X joe X""")
    
def displayWelcome():
    '''displays Welcome on screen'''
    print("Welcome")

def drawBox():
    '''prints a 7x5 box made of Xs w/ name joe in the middle'''
    drawSevenXs()
    drawTwoXs()
    drawXJoeX()
    drawTwoXs()
    drawSevenXs()
        
def displayThanks():
    '''displays Thanks on screen'''
    print("Thanks")

def drawBoxAndName():
    displayWelcome()
    drawBox()
    displayThanks()

def main():
    drawBoxAndName()
    os.system("pause")
    
if __name__ == '__main__':
    main()
