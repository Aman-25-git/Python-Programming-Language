#non-const.py
class Employee:
     def readempval(self):
         self.eno=100
         self.ename="RS"
#Main Program
eo=Employee()
print(eo.__dict__)
eo.readempval()
print(eo.__dict__)