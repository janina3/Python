from BankAccount import DEPOSIT_NEG
from BankAccount import WITHDRAW_NEG
from BankAccount import OVERDRAFT
from BankAccount import INVALID_TYPE

from BankAccount import BankAccount

#error codes
DUPLICATE_NUMBER = -5
INVALID_NUMBER = -6

#module level variable
NEXT_ACCT_NUM = 1000

class Bank(object):

    def __init__(self, name):
        self.__name = name
        self.__bankAccounts = {}

    def createBankAccount(self, name, acctType, balance = 0):
        accountNum = self.__getNextAccountNum()
        if accountNum in self.__bankAccounts:
            return DUPLICATE_NUMBER
        newBankAccount = BankAccount(accountNum, name, acctType, name)
        self.__bankAccounts[accountNum] = newBankAccount
        return accountNum

    def __getNextAccountNum():
        '''return NEXT_ACCT_NUM and set it to 2 more'''
        newAcctNumber = NEXT_ACCT_NUM
        global NEXT_ACCT_NUM
        NEXT_ACCT_NUM += 2
        return newAcctNumber

    def depositIntoAccount(self, accountNum, account):
        if accountNum not in self.__bankAccounts:
            return INVALID_NUMBER
        ret = self.__bankAccounts[accountNum].deposit(amount)
        if ret == DEPOSIT_NEG:
            return ret
        #can change this later
        return ret

    def withdrawFromAccount(self, accountName, amount):
        if accountNum not in self.__bankAccounts:
            return INVALID_NUMBER
        ret = self.__bankAccounts[accountNum].withdraw(amount)
        if ret == WITHDRAW_NEG:
            return ret
        if ret == OVERDRAFT:
            return ret
        #can change this later
        return ret

    def transfer(self, acctNumFrom, acctNumTo, amount):
        if(acctNumFrom not in self.__bankAccounts):
            return INVALID_NUMBER
        if(acctNumTo not in self.__bankAccounts):
            return INVALID_NUMBER
        
        #bankAccount method
        self.__bankAccounts[accountNumFrom]

        #bank method
        self.depositIntoAccount(acctNumTo, amount)
    
    def getMoneyInBank(self):
        totalFunds = 0.0
        for acctNumber in self.__bankAccounts:
            totalFunds += self.__bankAccounts[acctNumber]
        return totalFunds

    def __str__(self):
        stringRep = ''
        stringRep += self.__name
        for acctNum in self.__bankAccounts:
            stringRep += str(self.__bankAccounts[acctNum])
        return stringRep
