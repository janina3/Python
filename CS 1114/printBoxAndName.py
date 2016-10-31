#!/usr/bin/python/
'''
Programmer: Janina Soriano
Username: js7817

This prints out Welcome, a 7x5 box with 'joe' in the middle, then Thanks

'''

from __future__ import print_function

if __name__ == '__main__':
'''import os
    os.system("pause")
'''


def printBoxAndName():

    def printRow7Xs():
        """prints 7 Xs in a row"""
        print("""XXXXXXX""")
            
    def printRowWithSpace():
        """prints a row with an X in the beginning and an X in the end with 5 spaces between"""
        print("""X    X""")

    def printRowWithName():
        """prints X, space, jor, space X"""
        print("""X joe X""")
    
    def displayWelcome():
        '''displays Welcome on screen'''
        print("Welcome")

    def printBox():
        '''prints a 7x5 box made of Xs w/ name joe in the middle'''
        printRow7Xs()
        printRowWithSpace()
        printRowWithName()
        printRowWithSpace()
        printRow7Xs()
        
    def printThanks():
        '''prints Thanks on screen'''
        print("Thanks")

printBoxAndName()

def main():
    printWelcomeStatement()
    printBox
    printGoodbye

main()
