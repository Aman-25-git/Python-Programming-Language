#Program to read input form keyboard and save that data into file of secondary memory
#EmpPickleEx.py
import pickle
filename=input("Enter file name: ")
with open(filename, 'wb') as fp:
    while(1):
        empno=int(input("Enter Employee Number:"))
        empname=input("Enter Employee Name:")
        empsal=float(input("Enter Employee Salary:"))
        lst=list()
        lst.append(empno)
        lst.append(empname)
        lst.append(empsal)
        pickle.dump(lst,fp)
        ch=input("Do you want to continue?(y/n):")
        if ch.lower()=="n":
            break
print("We Succesfully Saved Employee Data")
