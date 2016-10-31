'''
cs1114

Submission: hw09

Programmer: Janina Soriano
Username: js7817

This program...

Assumptions: None
Constraints: None

The purpose of this program is...

'''

def openFile():
    '''Opens and returns txt file'''
    countryList = []
    txtFile = open('UN-world-pop-change-data.txt', 'r')
    for line in txtFile:
        countryList = line.strip('/t')

##        line = line.replace(',', '')
    print(countryList)
    return countryList

def convertToDict(countryList):
    '''Converts the passed in list into a dictionary'''
    countryYearsDict = {}
    countryData = countryList.split('/t')
    print(countryData)
    for i in countryList:
        countryYearsDict[i] = i + 1
        i += 1
    print(countryYearsDict)
        

##def printSummaryReport(yearRange, countryDict):
##    '''Prints the summary report for passed in information'''
##    print("%s Summary Report" % yearRange)
##    print("")
##    print("Average perfect change over all: %.3f%" % )
##    print("The three countries or regions with the largest change:")
##    print("%s (%.2f), %s (%.2f), %s (%.2f)" % )
##    print("The three countries or regions with the smallest change:")
##    print("%s (%.2f), %s (%.2f), %s (%.2f)" % )

def main():
    countryList = openFile()
    convertToDict(countryList)

if __name__ == '__main__':
    main()
