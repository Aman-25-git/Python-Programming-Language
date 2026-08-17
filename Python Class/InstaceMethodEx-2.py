#Program for Demonstrating Instance Method and 'self'
#InstaceMethodEx-1.py
class Student:
    def readsd(self,objinfo):
        print("Enter {} Student info".format(objinfo))
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.marks=float(input("Enter Marks:"))
    def dispsd(self,objinfo):
        print("{} Student info".format(objinfo))
        print("Student Number:",self.sno)
        print("Student Name:",self.sname)
        print("Marks:",self.marks)
#Main Program
s1=Student()
s2=Student()
print("Content of s1 Object=",s1.__dict__)
print("Content of s1 Object=",s2.__dict__)
print("-"*50)
s1.readsd("First")
print("-"*50)
s2.readsd("Second")
print("-"*50)
s1.dispsd("First")
print("-"*50)
s2.dispsd("Second")
print("-"*50)