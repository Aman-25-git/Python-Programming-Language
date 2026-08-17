#program for Demonstrating the Functionality of Class Level Methods
#ClassLevelMethodEx2.py
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="Python.Net"
        cls.getcity()
    @classmethod
    def getcity(cls):
        cls.city="Umami"

#Main Program
Student.getcrs()
print("Student Course:",Student.crs)
print("Student city:",Student.city)