#!/usr/bin/python

'''
Programmer: Janina Soriano
Username: js7817

filename: hw01.py

This program is the function main calling pre-defined functions that will print the first name of the user in a box "designed" by them, and same for their last name. It ends with a pre-written closing statement.


Constraints: None

Assumptions: None

'''

def main():
    (firstName) = getStrFromUser("What is your first name? ")
    (lastName) = getStrFromUser("What is your last name? ")
    (boxChar) = getStrFromUser("What character to use for the box? ")
    (fillChar) = getStrFromUser("What character to use to fill in the box? ")
    drawBoxAroundStr(firstName, boxChar, fillChar)
    drawBoxAroundStr(lastName, boxChar, fillChar)
    pythonicPause()

if __name__ == '__main__':
    main()
