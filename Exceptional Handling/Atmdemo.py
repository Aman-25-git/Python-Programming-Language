#Atmdemo.py<----Main program
from AtmMenu import menu
from Atmexecpt import DepositError,WithdrawError,InsuffFundError
from Atmop import Deposit,Withdraw,Balance
while(1):
    try:
        menu()
        ch=int(input("Enter your choice: "))
        match(ch):
            case 1:
                try:
                    Deposit()
                except DepositError:
                        print("\tDon't try Deposit -VE / Zero Values-try again")
                except InsuffFundError:
                    print("\tDon't Have Funds to Withdraw!!!--try again")
                except ValueError:
                    print("Don't Enter Allnums ,str's,special symbols only digits are allowed!!!--try again")

            case 2:
                    try:
                        Withdraw()
                    except WithdrawError:
                        print("\tDon't try Deposit -VE / Zero Values-try again")
                    except InsuffFundError:
                        print("\tDon't Have Funds to Withdraw!!!--try again")
                    except ValueError:
                        print("Don't Enter Allnums ,str's,special symbols only digits are allowed!!!--try again")

            case 3:
                Balance()
            case 4:
                print("Thanks for using this project")
                break
            case _:
                print("\tUr selection of option is worng!!!--try again")
    except ValueError:
        print("\tDon't Enter alnums,strs and symbols for Choice--try again")