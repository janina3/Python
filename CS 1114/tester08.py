#!/usr/bin/python

'''
cs1114

Submission: hw08

Programmer: Janina Soriano
Username: js7817

The purpose of this program is to test the listFunctions file.

Assumptions: Depends on the function
Constraints: None

This program uses many list functions to accomplish different tasks.

'''

import copy

from listFunctions import displayListElements
from listFunctions import returnMin
from listFunctions import returnMinIndex
from listFunctions import chopList
from listFunctions import returnCommonElements
from listFunctions import insertListIntoAnotherList

def main():
    testList = [3, 2, 7, -1]
    testList2 = [8, 4, 33]
    displayListElements(testList)
    print(returnMin(testList))
    print(returnMinIndex(testList))
    print(chopList(testList, 0, 2))
    print(insertListIntoAnotherList(testList, testList2))
    
    testList = [3, 2, 7, -1, 24, 47, -14, 4]
    testList2 = [8, 4, 33, -1, 2, 9, 3]
    print(returnCommonElements(testList, testList2))

    testList = [4, 2, 4, 4, 7, -1]
    testList2 = [8, 4, 33]
    print(insertListIntoAnotherList(testList, testList2))


if __name__ == '__main__':
    main()
    
