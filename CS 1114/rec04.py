def printAsUSDollars(moneyAmt, sign):
    '''prints the amount in US dollars

       sign must be either $ or USD (with space after USD)       
    
    '''
    print ("%s%i" % (sign, moneyAmt))

def convertPesosToUSDollars(pesosAmt):
    '''returns the pesos amount in dollars'''
    conversionRate = .075
    dollarConversion = pesosAmt / conversionRate
    return("$%.2f" % (dollarConversion))

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
    numCoins = numDollarCoins + numQuarters + numDimes + numNickels + numPennies
    print("%i dollar coin(s), %i quarter(s), %i dime(s), %i nickel(s), %i penny(pennies)" % (numDollarCoins, numQuarters, numDimes, numNickels, numPennies)) 


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
    numCoins = numDollarCoins + numQuarters + numDimes + numNickels + numPennies
    print ("%i coins" % (numCoins))
    return(moneyAmt, numDollarCoins, numQuarters, numDimes, numNickels, numPennies)
    
