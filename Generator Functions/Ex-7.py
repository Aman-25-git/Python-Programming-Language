#Program to generate otp
#Ex-7
import random as aman
def getotp():
    while(1):
        yield "ur otp is: {}".format(aman.randint(30000,50000))
        n=n+1
#main program
dr=getotp()
print(next(dr))