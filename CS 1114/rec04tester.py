#!/usr/bin/python

'''
Programmer: Janina Soriano
Username: js7187

Constraints: None

Assumptions: None

'''

from rec04 import printAsUSDollars
from rec04 import convertPesosToUSDollars
from rec04 import printAsCoins
from rec04 import quantityOfCoins


def moneyChanger():
    '''runs rec04 to test it'''
    moneyAmt = 75.63
    pesosAmt = 10000
    sign = "$"
    printAsUSDollars(moneyAmt, sign)
    convertPesosToUSDollars(pesosAmt)
    (moneyAmt, numDollarCoins, numQuarters, numDimes, numNickels, numPennies) = quantityOfCoins(moneyAmt)
    printAsCoins(moneyAmt)
    
def main():
    moneyChanger()

main()
