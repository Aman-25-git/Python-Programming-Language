#Program to Storing stno,marks and name of a student by using class and objects
#InstanceDataMemberEx-1.py
class Student:
    pass
#Main Program
#Create two Student objects
s1=Student()
s2=Student()
#Store data to that object s1
s1.sno=200
s1.sname="Guido van Rossom"
s1.marks=34.56
#Store data to that object s2
s2.sno=200
s2.sname="Pulla vinay"
s2.marks=34.56
#Display the content
print("-"*50)
print("Content of s1 object")
print("-"*50)
print("\tStudent number is{}".format(s1.sno))
print("\tStudent name is{}".format(s1.sname))
print("\tStudent marks is{}".format(s1.marks))
print("-"*50)
print("-"*50)
print("Content of s2 object")
print("-"*50)
print("\tStudent number is{}".format(s2.sno))
print("\tStudent name is{}".format(s2.sname))
print("\tStudent marks is{}".format(s2.marks))
print("-"*50)
