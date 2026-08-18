#Employeepick.py
import Employee
import pickle
class EmployeePick:
    def getemployee(self):
        print("--------------------------")
        self.eno=int(input("Enter Employee Number:"))
        self.name=str(input("Enter Employee Name:"))
        self.sal=float(input("Enter Employee Salary:"))
    def saveempdata(self):
        with open("emp.pickle","ab") as fp:
            e1=Employee.Employee(self.eno,self.name,self.sal)
            pickle.dump(e1,fp)
            print("Employee saved")

#Main Program
ep=EmployeePick()
ep.getemployee()
ep.saveempdata()
