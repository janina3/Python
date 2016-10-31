#!/usr/bin/python

'''
cs1114

Submission: rec11

Programmer: Janina Soriano
Username: js7817

The purpose of this program is to work with HTML files.

Assumptions: Depends on the function
Constraints: None

This program creates an HTML file.

'''

import random

def openMyFile():
    '''Opens and returns my HTML file'''
    wordList = []
    htmlFile = open('rec11List.txt', 'r')
    for line in htmlFile:
        wordList.append(line[:-1])
    return wordList

def openColorList():
    '''Opens and returns the colors HTML file'''
    colorList = []
    htmlFile = open('colorNames.txt', 'r')
    for line in htmlFile:
        colorList.append(line[:-2])
    return colorList
    
def createHTMLFile(wordList, htmlColors):
    '''Creates a customized HTML file'''
    fileName = (str(raw_input("Enter a file name: ")) + ".html")
    newFile = open(fileName, 'w')

    headingSize = int(raw_input("Enter a heading size for the title: "))

    newFile.write('''

    <html>
    <H%i><b>%s</b></H%i>
    </html>''' % (headingSize, fileName, headingSize))

    fileWithWords = open(fileName, "a")
    previousColor = ''
    for word in wordList:
        randHeadingSize = random.randint(1, 5)
        randColor = random.choice(htmlColors)
        if(randColor == previousColor):
            randColor = random.choice(htmlColors)
        fileWithWords.write('''

    <html>
    <font color = %s><H%i>%s</H%i></font>
    </html>''' % (randColor, randHeadingSize, word, randHeadingSize))
        previousColor = randColor

def main():
    wordList = []
    htmlColors = []
    wordList = openMyFile()
    htmlColors = openColorList()
    createHTMLFile(wordList, htmlColors)

if __name__ == '__main__':
    main()

