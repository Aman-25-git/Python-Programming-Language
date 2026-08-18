#Program to demonstrate Constructor
#constructor.py
class Employee:
    def __init__(self):
        self.eno=90
        self.ename="Ranjith"


#Main Program
eo=Employee()#When object creates then it search for constructor in class
print(eo.__dict__)
e1=Employee()
print(e1.__dict__)
e2=Employee()
print(e2.__dict__)