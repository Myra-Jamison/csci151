#------------------------------------------------
# Bank Account Classes: Assignment 12
# ------------------------------------------------
# Myra Jamison (Late)
# CSCI 151

import stdio

#This is a module that creates a class called BankAccount with methods
#that allow for common bank account operations

#class definition
class BankAccount:
    def __init__(self, acct_holder, acct_num, balance):
        #instance variables
        self._acct_holder = acct_holder
        self._acct_num = int(acct_num)
        self._balance = float(balance)

    #get acct holder name and print to stdout
    def get_account_holder_name(self):
        return stdio.writeln('Account Holder Name: '+
                             str(self._acct_holder))
    
    #deposit money into the owners bank account
    def deposit(self, amount):
        if amount <= 0:
            return stdio.writeln('Invalid deposit amount')
        self._balance += amount
        return stdio.writeln(str(self._acct_holder) +
                             ' deposited $' + str(amount) +
                             '. New balance: $' + str(self._balance))

    #withdraw money from the owners account
    def withdraw(self, amount):
        if self._balance - amount <= 0 or amount <= 0:
            return stdio.writeln('Insufficient balance or invalid deposit amount')
        self._balance -= amount
        return stdio.writeln(str(self._acct_holder) +
                             ' withdrew $' + str(amount) +
                             '. New balance: $' + str(self._balance))
    
    #get acct balance
    def get_balance(self):
        return stdio.writeln('Account Balance: $'+
                             str(self._balance))
    
    #transfer money from owners account to another individuals account with object name 'party'
    def transfer(self,party,amount):
        if self._balance - amount <= 0 or amount <= 0:
            return stdio.writeln('Insufficient balance or invalid deposit amount')
        self.withdraw(amount)
        party.deposit(amount)
        return stdio.writeln(str(self._acct_holder) + ' transferred $' +
                             str(amount) + ' to ' + str(party._acct_holder))
    
    #string summary of object using __str__ name
    def __str__(self):
        return str('New Account:\n'+'Number: ' +
                             str(self._acct_holder) + '\n' +
                             'Holder: ' + str(self._acct_num) + '\n' +
                             'Balance: $' + str(self._balance))

#test client, tests all of the method functions
def main():
    stdio.writeln("*Testing account creation for Alice and Bob, and str output:")
    alice = BankAccount('Alicia', 1234567, 50)
    stdio.writeln(str(alice))
    bob = BankAccount('Robert', 1234568, 100)
    stdio.writeln(str(bob))
    stdio.writeln("-------------------\n" +
                  "*Testing Getting Names:")
    alice.get_account_holder_name()
    bob.get_account_holder_name()
    stdio.writeln("-------------------\n" +
                  "*Testing Deposit (Bob Invalid, Alice Valid):")  
    alice.deposit(25)
    bob.deposit(-4) 
    stdio.writeln("-------------------\n" +
                  "*Testing Withdraw (Bob Invalid, Alice Valid):")  
    alice.withdraw(7.5)
    bob.withdraw(-30)
    stdio.writeln("-------------------\n" +
                  "*Testing Transfer (Bob Invalid, Alice Valid):")
    alice.transfer(bob,30)
    bob.transfer(alice,5000)
    stdio.writeln("-------------------\n" +
                  "*Testing Getting Balance:")
    alice.get_balance()
    bob.get_balance()
    return stdio.writeln("*Check complete")

#test client
if __name__ == "__main__":
    main()