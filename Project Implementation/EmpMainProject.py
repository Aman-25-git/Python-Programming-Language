#EmpMainProject.py<--- Module Name
from EmpMenu import menu
from EmpAdd import addemployee
from EmpView import viewemployee,viewsingleemployee
from EmpSearch import searchemployee
from EmpUpdate import updateEmployee
from EmpDelete import deleteEmployee
while(True):
    menu()
    try:
        ch=int(input("Enter ur Choice:"))
        print("-"*50)
        match(ch):
            case 1:
                addemployee()
            case 2:
                deleteEmployee()
            case 3:
                updateEmployee()
            case 4:
                viewsingleemployee()
            case 5:
                viewemployee()
            case 6:
                searchemployee()
            case 7:
                print("Thanks For Using This Program")
                exit()
            case _:
                print("Entered Choice is Invalid ---Try Again")
    except ValueError:
        print("only digits are allowed(from 1-7)")