#Muldemo.py<----main program
from Mulexcept import AmanZeroError,NegativeError
from multiply import table
while(1):
    try:
        table(int(input("Enter a number to print it's table:")))
        break
    except NegativeError:
        print("\tDon't Enter negative values as input!!!!--try again")
    except AmanZeroError:
        print("\tDon't enter Zero's as values as input!!!!--try again")
    except ValueError:
        print("\tDon't Enter allnums,special,str only digits are allowed!!!!--try again")
