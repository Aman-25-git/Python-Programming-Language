#divdemo.py<---Main Program
from Divexcept import AmanZeroError
from division import division
while(1):
    try:
        a=float(input("Enter a number: "))
        b=float(input("Enter another number: "))
        res=division(a,b)
    except AmanZeroError:
        print("Don't Enter Zero's as Denominator!!--try again")
    except ValueError:
        print("Don't Enter str only digits allowed!--try again")
    else:
        print(" Division={}".format(res))
        break
    finally:
        print("Thanks for using this program.")
