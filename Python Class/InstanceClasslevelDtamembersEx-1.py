#program for Storing stno,name ,marks along with Common Value Course and City By using Classes and Objects
#InstanceClasslevelDtamembersEx-1.py
class Student:
    city="Ahmedhabad"
    crs="Python"
#Main Program
s1=Student()
s2=Student()

s1.sno=90
s1.sname="Travis"
s1.marks=45.67

s2.sno=90
s2.sname="Hunter"
s2.marks=45.74
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