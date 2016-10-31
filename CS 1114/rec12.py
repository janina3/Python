#!/usr/bin/python

'''
cs1114

Submission: rec12

Programmer: Janina Soriano
Username: js7817

The purpose of this program is to

Assumptions: 
Constraints: None

This program 

'''

import os

def getInputFile():
    '''The user chooses a file to input'''
    validFilename = str(raw_input("Enter a filename: "))
    if(not os.path.exists("/Users/janinasoriano/Documents/School Work/NYU Freshman/CS 1114/" + validFilename)):
        validFilename = str(raw_input("Not a valid filename. Enter a filename: "))
    userFile = open(validFilename, 'r')
    return userFile

def outputFile():
    '''The user chooses a name for the output file'''
    validFilename = str(raw_input("Enter a new filename: "))
    if(os.path.exists("/Users/janinasoriano/Documents/School Work/NYU Freshman/CS 1114/" + validFilename)):
        choice = str(raw_input("This filename already exists. Do you want to overwrite it? "))
        choice = choice.lower()
        if(choice == 'n' or choice == 'no'):
            validFilename = str(raw_input("Enter another filename: "))
    newFile = open(validFilename, 'w+')
    return newFile

def between():
    '''Gets a word from the user for between'''
    betweenWord = str(raw_input("Enter a word for between: "))
    return betweenWord

def processFile(userFile, newFile, betweenWord):
    '''Replaces blank space with a word of the user's choice'''
    for line in userFile:
        fileList = line.split()
        newLines = betweenWord.join(fileList)
        newFile.write(newLines + '\n')

def main():
    userFile = getInputFile()
    newFile = outputFile()
    betweenWord = between()
    processFile(userFile, newFile, betweenWord)

    

if __name__ == '__main__':
    main()
