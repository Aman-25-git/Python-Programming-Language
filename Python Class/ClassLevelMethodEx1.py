#program for Demonstrating the Functionality of Class Level Methods
#ClassLevelMethodEx1.py
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="Python.Net"
    @classmethod
    def getcity(cls):
        cls.city="Umami"

#Main Program
Student.getcrs()
Student.getcity()
print("Student Course:",Student.crs)
print("Student city:",Student.city)