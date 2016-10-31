#!/usr/bin/python

'''
Programmer: Janina Soriano
Username: js7187

Constraints: None

Assumptions: None

'''

from rec04 import printAsUSDollars
'''
from rec04 import convertPesosToUSDollars
'''
from rec04 import printAsCoins
from rec04 import quantityOfCoins

def tester():
    '''calls the functions in rec04.py to test them'''
    moneyAmt = int(raw_input("Money Amount: "))
    return moneyAmt
    sign = int(raw_input("Choose $ or USD (with space after USD): "))
    return sign
    pesosAmt = int(raw_input("Pesos Amount: "))
    return pesosAmt

def moneyChanger():
    '''runs rec04 to test it'''
    (moneyAmt, sign, pesosAmt) = tester()
    printAsUSDollars(moneyAmt, sign)
    convertPesosToUSDollars(pesosAmt)
    (moneyAmt, numDollarCoins, numQuarters, numDimes, numNickels, numPennies) = quantityOfCoins(moneyAmt)
    printAsCoins(numDollarCoins, numQuarters, numDimes, numNickels, numPennies)
    
def main():
    
    moneyChanger()

main()
