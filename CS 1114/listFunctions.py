#!/usr/bin/python

'''
cs1114

Submission: hw08

Programmer: Janina Soriano
Username: js7817

The purpose of this program is to utilize the different capabilities of lists.

Assumptions: Depends on the function
Constraints: None

This program uses many list functions to accomplish different tasks.

'''

import copy

def displayListElements(passedList):
    '''This function displays the elements in a passed in list, one per line'''
    for element in passedList:
        print(element)

def returnMin(passedList):
    '''This function returns the minimum value in a passed in list. Assume all elements are numeric values'''
    minVal = passedList[0]
    if(passedList[0] > passedList[1]):
        minVal = passedList[1]
    for element in passedList:
        if(minVal > element):
            minVal = element
    return minVal

def returnMinIndex(passedList):
    '''This function returns the index of the minimum value in a passed in list. Assume all elements are numeric values'''
    minIndex = 0
    for i in range(len(passedList)):
        if(passedList[minIndex] > passedList[i]):
            minIndex = i
    return minIndex

def chopList(listName, leftEnd, rightEnd):
    '''This function chops out a subsequence of a passed in list given the list and the endpoints'''
    listName = listName[leftEnd:rightEnd]
    return listName

'''-------------------------------------------------------'''

def returnCommonElements(list1, list2):
    '''This function takes two lists and returns a list of the common elements in the same order as the first parameter'''
    commonElements = []
    for i in list1:
        if(i in list2):
            commonElements.append(i)
    return commonElements

'''-------------------------------------------------------'''

def insertListIntoAnotherList(list1, list2):
    '''This function takes two lists, reorders the first list into descending numeric order, then splices the second list's elements into the first list in the correct place, then returns that list. Assume both lists only contain numeric values'''
    addAfterVal = "No"
    
    list1Sorted = copy.deepcopy(list1)
    list2MinVal = returnMin(list2)
    
    addIndex = list1Sorted.count(list2MinVal)
        
    list1Sorted.append(list2MinVal)
    list1Sorted.sort()
    list1Sorted.reverse()
    
    list2Index = list1Sorted.index(list2MinVal) + addIndex
        
    list1Sorted.remove(list2MinVal)
    
    list1Sorted[list2Index:list2Index] = list2
 
    return list1Sorted
