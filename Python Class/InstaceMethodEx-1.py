#Program for Demonstrating Instance Method and 'self'
#InstaceMethodEx-1.py
class Student:
    def readsd(self):
        print("readsd()--Address of currrect object",id(self))

#Main Program
s1=Student()
print("Memery address of s1 object is:",id(s1))
s1.readsd()
s2=Student()
print("Memery address of s2 object is:",id(s2))
s2.readsd()