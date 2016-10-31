'''
cs1114

Submission: hw10-company.py

Programmer: Janina Soriano
Username: js7817

This program...

Assumptions: None
Constraints: None

The purpose of this program is...

'''

from hw10-worker import WorkerRecord

class Company(object):

    def __init__(self, companyName):
        self.__companyName = companyName
        self.__workerRecord = {}

    def getCompanyName(self):
        '''Returns the name of the company'''
        return self.__companyName

    def getWorkerRecord(self):
        '''Returns the worker record'''
        return self.__workerRecord

    def changeCompanyName(self, newCompanyName):
        '''Returns the company's new name'''
        self.__companyName = newCompanyName

    def addWorker(self, ssn, name, workerRecord):
        '''Adds a worker to the worker record if the SSN isn't already in the system'''
        '''Adds the ssn and information to the ssn dictionary if the ssn isn't already in it'''
        if ssn in workerRecord.keys:
            return DUPLICATE_SSN
        newWorkerRecord = WorkerRecord(self, ssn, name)
        self.__workerRecord[ssn] = newWorkerRecord

    def addHours(self, newHours):
        '''Returns the new hours of the employee'''
        hours = addHours(self, newHours)
        return hours

    def changeTitle(self, newTitle):
        '''Returns the new title of the employee'''
        title = changeTitle(self, newTitle)
        return title

    def changePayRate(self, newPayRate):
        '''Returns the new pay rate'''
        payRate = changePayRate(self, newPayRate)

    def payWorkers(self, workerRecord):
        '''Creates and sends a file to the accounting department'''
        filename = str(raw_input("Enter a filename: "))
        newFile = open(filename, 'w')

        for ssn in workerRecord:
            worker = workerRecord[ssn]
            name = worker.getName()
            title = worker.getTitle()
            earnings = worker.earnings()
            print(ssn)
            if(title != null):
                print("%s $%.2f [%s]" % (name, earnings, title))
            else:
                print("%s $%.2f" % (name, earnings))

    def fireWorker(self, ssn, WorkerRecord):
        '''Pays the worker for the hours they've worked, then removes them from the Worker Record'''
        
        
            
        
