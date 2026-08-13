#EmpAdd.py<----Module Name
import pickle
def addemployee():
        try:
            with open("EmpProject.data","ab")as fp:
                print("-"*50)
                eno=int(input("Enter Employee Number:"))
                ename=input("Enter Employee Name:")
                esal=float(input("Enter Employee Salary:"))
                lst=[]
                lst.append(eno)
                lst.append(ename)
                lst.append(esal)
                pickle.dump(lst,fp)
                print("-"*50)
                print("Employee Added Successfully")
                print("-"*50)
        except ValueError:
            print("Please enter a valid number/name/salary")
