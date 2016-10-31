#!/usr/bin/python

'''
Programmer: Janina Soriano
Username: js7187

Constraints: None

Assumptions: None

'''

def quantityOfCoins(moneyAmt):
    '''prints the total number of coins and returns the number of coins of each denomination if the money were converted'''
    numDollarCoins = moneyAmt // 1
    newMoneyAmt = moneyAmt - 1 * numDollarCoins
    numQuarters = newMoneyAmt // 0.25
    newMoneyAmt = newMoneyAmt - 0.25 * numQuarters
    numDimes = newMoneyAmt // 0.10
    newMoneyAmt = newMoneyAmt - 0.10 * numDimes
    numNickels = newMoneyAmt // 0.05
    newMoneyAmt = newMoneyAmt - 0.05 * numNickels
    numPennies = newMoneyAmt // 0.01
    '''numCoins = numDollarCoins + numQuarters + numDimes + numNickels + numPennies'''
    '''print ("%i coins" % (numCoins))'''
    return(moneyAmt, numDollarCoins, numQuarters, numDimes, numNickels, numPennies)
    
def printAsCoins(moneyAmt):
    '''displays the number of coins of each denomination if the money were converted'''
    numDollarCoins = moneyAmt // 1
    newMoneyAmt = moneyAmt - 1 * numDollarCoins
    numQuarters = newMoneyAmt // 0.25
    newMoneyAmt = newMoneyAmt - 0.25 * numQuarters
    numDimes = newMoneyAmt // 0.10
    newMoneyAmt = newMoneyAmt - 0.10 * numDimes
    numNickels = newMoneyAmt // 0.05
    newMoneyAmt = newMoneyAmt - 0.05 * numNickels
    numPennies = newMoneyAmt // 0.01
    '''numCoins = numDollarCoins + numQuarters + numDimes + numNickels + numPennies'''
    '''print("%i dollar coin(s), %i quarter(s), %i dime(s), %i nickel(s), %i penny(pennies)" % (numDollarCoins, numQuarters, numDimes, numNickels, numPennies))'''
    if numDollarCoins > 0:
        print("%i dollar coin(s)" % (numDollarCoins))
    if numQuarters > 0:
        print("%i quarters(s)" % (numQuarters))
    if numDimes > 0:
        print("%i dime(s)" % (numDimes))
    if numNickels > 0:
        print("%i nickel(s)" % (numNickels))
    if numPennies > 0:
        print("%i penny(ies)" % (numPennies))

def main():
    quantityOfCoins(moneyAmt)
    printAsCoins(moneyAmt)

#main()
