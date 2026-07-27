#NameValidationDemo.py
from NameExcept import ZeroNameLengthError, InValidNameError, SpaceError
from NameValidation import validate_name
while(True):
    try:
        name=input("Enter your name: ")
        vname=validate_name(name)
    except ZeroNameLengthError:
        print("\tU Must Enter UR Name-try again")
    except InValidNameError:
        print("\tUr Name is Invalid-try again")
    except SpaceError:
        print("\tDon't enter Space for Ur Name-try again")
    else:
        print("\tUR Valid name=",vname)
        break
