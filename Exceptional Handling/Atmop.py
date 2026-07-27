#Atmop<----Module name
from Atmexecpt import *
bal=500.00
def Deposit():
    damt =float(input("Enter Deposit Amount: "))
    if (damt < 0):
       raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUR Account xxxxxxx123 Credited after deposit with INR:{}".format(damt))
        print("\tNow UR Account xxxxxxx123 with INR:{}".format(bal))
def Withdraw():
    global bal
    wamt = float(input("Enter Withdraw Amount: "))
    if (wamt <= 0):
        raise WithdrawError
    elif(wamt>bal):
        raise InsuffFundError
    else:

        bal=bal-wamt
        print("\tUR Account xxxxxxx123 Debited after Withdraw with INR:{}".format(wamt))
        print("\tNow UR Account xxxxxxx123 with INR:{}".format(bal))


def Balance():
    print("\tNow UR Account xxxxxxx123 with INR:{}".format(bal))

