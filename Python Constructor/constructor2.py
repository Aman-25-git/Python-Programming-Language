#Program to demonstrate construtor
#constructor2.py
class Employee:
    def __init__(self,a,b):#Parameterized constuctor
        self.no=a
        self.name=b
#Main Program
e1=Employee(10,"JS")
e2=Employee(45,"OS")
print(e1.__dict__)
print(e2.__dict__)