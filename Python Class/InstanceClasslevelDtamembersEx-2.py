#program for Storing stno,name ,marks along with Common Value Course and City By using Classes and Objects
#InstanceClasslevelDtamembersEx-1.py
class Student:
    city="Ahmedhabad"
    crs="Python"
#Main Program
s1=Student()
s2=Student()

s1.sno=int(input("Enter Student 1 number:"))
s1.sname=input("Enter Student 1 name:")
s1.marks=float(input("Enter Student 1 marks:"))

s2.sno=int(input("Enter Student 2 number:"))
s2.sname=input("Enter Student 2 name:")
s2.marks=float(input("Enter Student 2 marks:"))
print("S1 DATA:")
print("\tStudent number:{}".format(s1.sno))
print("\tStudent name:{}".format(s1.sname))
print("\tStudent marks:{}".format(s1.marks))
print("\tStudent city:{}".format(Student.city))
print("\tStudent Course:{}".format(Student.crs))
print("-"*50)
print("S2 DATA:")
print("\tStudent number:{}".format(s2.sno))
print("\tStudent name:{}".format(s2.sname))
print("\tStudent marks:{}".format(s2.marks))
print("\tStudent city:{}".format(Student.city))
print("\tStudent Course:{}".format(Student.crs))
print("-"*50)
print("-"*50)
print("Content of s1 object=",s1.__dict__)
print("Number of values in s1 object=",len(s1.__dict__))
print("-"*50)
print("Content of s2 object=",s2.__dict__)
print("Number of values in s2 object=",len(s2.__dict__))