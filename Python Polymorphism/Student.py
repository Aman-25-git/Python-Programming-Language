#Student.py
from univer import univ
from college import College
class Student(College):
    def getdata(self):
        self.sno=input("Enter Student Number:")
        self.sname=input("Enter Student Name:")
        self.crs=input("Enter Student CRS:")
        super().getdata()
    def dispdata(self):
        univ.dispdata(self)
        College.dispdata(self)
        print("----------------------------")
        print("Student Details")
        print("----------------------------")
        print("Student Name:", self.sname)
        print("Student CRS:", self.crs)
        print("Student Number:", self.sno)
        print("----------------------------")