class BankAccount:
    accountName = None
    accountNumber = None 
    bankName = None 
    branch = None
    balance = None 

    def __init__(self,accountName,accountNumber,branch,balance,bankName):
        self.__accountNumber = accountNumber # account number is private
        self.__accountName = accountName
        self.bankName = bankName
        self.__balance = balance
        self.__branch = branch
    
    def getAccountNumber(self):
        return f"Your  bank account number is {self.__accountNumber}"
    
    def getAccountName(self):
        return f"Your account name is {self.__accountName}"
    
    def getBalance(self):
        return f" Your balance is {self.__balance}"

    def getBranch(self):
        return f" Your branch is {self.__branch}"   


person1 = BankAccount(accountName="Mohd Hamza",accountNumber=939383920,branch='Kareli',balance=20000,bankName='Union Bank')

# direct accessing attributes

print(person1.accountName)
# person1.accountName = 'fsdfs'
# print(person1.accountName)
# print(person1.__accountNumber) # attribute error 
print(person1.accountNumber)
print(person1.balance)
print(person1.branch)
print(person1.bankName)

# accessing via methods 

print(person1.getAccountNumber())
print(person1.getAccountName())
print(person1.getBalance())
print(person1.getBranch())