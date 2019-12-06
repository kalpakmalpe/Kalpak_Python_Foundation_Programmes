#create the class Account

class Account:
    def __init__(self,acno,name,currbal):
        self.acno=acno
        self.name=name
        self.currbal=currbal


    def display(self):
        print("Account No:",self.acno)
        print("Name:", self.name)
        print("Current balance:", self.currbal)
        #print("new with deposit:",self.currbal+self.amount)
        #print("new withdraw:", self.currbal - self.amt)


    def deposite(self,amt):
        self.currbal+=amt
        print("Balance to be Deposit:",amt)



    def withdraw(self,amt):

        if (self.currbal<amt):
            print("insufficient balance......")
        else:
            self.currbal-=amt
            print("Balance to be Withdraw:",amt)


    def __del__(self):
        print("---------------------------------------------")





#create the object
a=Account(111,"kalpak",5000)
a.display()

a.deposite(200)
a.display()

a.withdraw(40000)
a.display()


