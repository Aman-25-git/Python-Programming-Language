#SameclassAccountEx2.py
class Account:
    def __init__(self):
        self.__acno=int(input("Enter Account Number :"))
        self.name=input("Enter Account Name :")
        self.__balance=int(input("Enter Account Balance :"))
        self.__pin=int(input("Enter Account Pin :"))
        self.brname=input("Enter Account Branch Name :")
    def getdata(self):
        print("-" * 50)
        print("Account Number :", self.__acno)
        print("Account holder name:", self.name)
        print("Account balance:", self.__balance)
        print("Account Pin :", self.__pin)
        print("Account Branch Name:", self.brname)
        print("-" * 50)
#Main Program
cs=Account()
cs.getdata()
