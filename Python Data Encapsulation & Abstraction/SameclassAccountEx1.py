#SameclassAccountEx1.py
class Account:
    def __init__(self):
        self.__acno=1234
        self.name="SAI"
        self.__balance=1000
        self.__pin=4567
        self.brname="Sebi"
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
