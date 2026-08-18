#Others5_6.py<------Program<--Data Abstraction
from Account5 import __Account
#ImportError: cannot import name 'Account' from 'Account5'
#This Program will not Execute bcoz Class Name made as Encapsulated
ac=__Account() # Object Creation
print("-"*50)
#print("Account Number:",ac.acno)
print("Account Holder Name:",ac.cname)
#print("Account Balance:",ac.bal)
#print("Account PIN:",ac.pin)
print("Account Branch Name:",ac.bname)
print("-"*50)