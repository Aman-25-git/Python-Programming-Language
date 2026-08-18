#Program to declare both constructors in one class
#DefaultParameterizedconst.py
class Test:
    def __init__(self,a=1,b=2):
        self.a=a
        self.b=b
        print("Value of a:", a)
        print("Value of b:", b)
        print("-------------------")
#Main Program
t1=Test(23)
t2=Test(b=5)
t3=Test(a=897)