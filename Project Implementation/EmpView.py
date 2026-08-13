#EmpView.py
import pickle
def viewemployee():
    with open("EmpProject.data","rb") as fp:
        print("-" * 50)
        print("\tEmpNo EmpName Empsal")
        print("-" * 50)
        while True:
            try:
                records=pickle.load(fp)
                for record in records:
                    print("\t",record,end=" ")
                print()
            except FileNotFoundError:
                print("File Not Found")
            except EOFError:
                print("-"*50)
                break
def viewsingleemployee():
    with open("EmpProject.data","rb") as fp:
        empno=int(input("Enter Employee Number:"))
        while True:
            try:
                records=pickle.load(fp)
                found=False
                if(records[0]==empno):
                    print("\tEmployee Number:",records[0])
                    print("\tEmployee Name:",records[1])
                    print("\tEmployee Salary:",records[2])
                    found = True
                    break
            except FileNotFoundError:
                print("File Not Found")
            except EOFError:
                print("-"*50)
                break
        if not found:
            print("Employee Number Not Found")


