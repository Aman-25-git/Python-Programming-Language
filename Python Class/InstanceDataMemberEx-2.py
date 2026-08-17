#Program to Storing stno,marks and name of a student by using class and objects
#InstanceDataMemberEx-2.py
class Student:
    pass
#Main Program
#Create two Student objects
s1=Student()
s2=Student()
print("-"*50)
print("Content of s1 object=",s1.__dict__)
print("Number of values in s1 object=",len(s1.__dict__))
print("-"*50)
print("Content of s2 object=",s2.__dict__)
print("Number of values in s2 object=",len(s2.__dict__))
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
print("\tStudent 1 {}".format(s1.__dict__))

print("-"*50)
print("-"*50)
print("Content of s2 object")
print("-"*50)
print("\tStudent 2 {}".format(s2.__dict__))

print("-"*50)

print("Content of s1 object=",s1.__dict__)
print("Number of values in s1 object=",len(s1.__dict__))
print("-"*50)
print("Content of s2 object=",s2.__dict__)
print("Number of values in s2 object=",len(s2.__dict__))