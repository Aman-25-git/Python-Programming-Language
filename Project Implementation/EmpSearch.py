#EmpSearch.py
import pickle
def searchemployee():
    with open("EmpProject.data", "rb") as fp:
        empno = int(input("Enter Employee Number:"))
        print("-" * 50)
        print("\tEmpNo EmpName EmpSal")
        print("-" * 50)
        while(True):
            try:
                records=pickle.load(fp)
                found=False
                if(records[0]==empno):
                    print("Valid Employee")
                    found=True
                    break
            except EOFError:
                break
        if (not found):
            print("Invalid Employee")
