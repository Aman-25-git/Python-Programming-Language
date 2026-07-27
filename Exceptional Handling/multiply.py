#multiply<----Module name
from Mulexcept import AmanZeroError,NegativeError
def table(n):
    if (n == 0):
       raise AmanZeroError
    elif(n<0):
        raise NegativeError
    else:
        print("-"*50)
        print("Multiplication Table for {}".format(n))
        print("-"*50)
        for i in range(1,11):
            print("{} x {} = {}".format(n,i,n*i))
        print("-"*50)