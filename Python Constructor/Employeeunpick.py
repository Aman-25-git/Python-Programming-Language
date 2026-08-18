#Employeeunpick.py
import pickle
class EmployeeUnpick:
    def readempdata(self):
        try:
            with open("emp.pickle","rb") as fp:
                while True:
                    try:
                        record=pickle.load(fp)
                        record.dispempdata()
                    except EOFError:
                        break
        except FileNotFoundError:
            print("emp.pickle file not found")

#Main Program
epo=EmployeeUnpick()
epo.readempdata()