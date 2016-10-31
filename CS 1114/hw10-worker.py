'''
cs1114

Submission: hw10-worker.py

Programmer: Janina Soriano
Username: js7817

This program...

Assumptions: None
Constraints: None

The purpose of this program is...

'''

DUPLICATE_SSN = -5

class WorkerRecord(object):

    def __init__(self, ssn, name, title = null, payRate = 17.22, hours = 0, earnings = 0):
        self.__ssn = ssn
        self.__name = name
        self.__title = title
        self.__payRate = payRate
        self.__hours = hours
        self.__earnings = earnings

    def getSSN(self):
        '''Returns ssn'''
        return self.__ssn

    def getName(self):
        '''Returns the name of the person with that SSN'''
        return self.__name

    def getTitle(self):
        '''Returns the title of the SSN'''
        return self.__title

    def getPayRate(self):
        '''Returns the pay rate of the SSN'''
        return self.__payRate

    def getHours(self):
        '''Returns the hours of the SSN'''
        return self.__hours

    def addHours(self, newHours):
        '''Returns the new hours of the employee'''
        self.__hours += newHours

    def changeTitle(self, newTitle):
        '''Returns the new title of the employee'''
        self.__title = newTitle

    def changePayRate(self, newPayRate)
        '''Returns the new pay rate'''
        self.__payRate = newPayRate

    def getPaid(self, hours, payRate):
        '''Returns the worker's earnings'''
        self.__earnings = payRate * hours

    def printWorkerRecord(self, ssn, name, title, payRate, hours):
        '''Prints out one worker's record'''
        print("Record for %i" % ssn)
        print("Name: %s" % name)
        print("Title: %s" % title)
        print("Pay Rate: %.2f/hour" % payRate)
        print("Hours: %i" % hours)
        print("Earnings: %.2f" % earnings)
    

   
