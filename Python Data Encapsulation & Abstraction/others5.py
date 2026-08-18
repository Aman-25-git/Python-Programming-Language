#Other5.py<----Data Abstraction
from Account5 import Account5#ImportError: cannot import name 'Account5' from 'Account5'
ac=Account5()
print("-"*50)
print("Account Number :",ac.ano)#this program is not executed bcoz , acno,balance,pin are encapsulated
print("Account holder name:",ac.name)
print("Account balance:",ac.balance)
print("Account Pin :",ac.pin)
print("Account Branch Name:",ac.brname)
print("-"*50)