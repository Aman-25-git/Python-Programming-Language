#InstanceClassLeveMethodEx1.py
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs = "Python.Net"
        cls.getcity()

    @classmethod
    def getcity(cls):
        cls.city = "Umami"

    def readsd(self,objinfo):
        print("Enter {} Student info".format(objinfo))
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.marks=float(input("Enter Marks:"))
    def dispsd(self,objinfo):
        Student.getcrs()
        print("{} Student info".format(objinfo))
        print("Student Number:",self.sno)
        print("Student Name:",self.sname)
        print("Marks:",self.marks)
        print("\tSTUDENT COURSE=", Student.crs)
        print("\tSTUDENT CITY=", Student.city)
# Main Program
s1=Student()
s1.readsd("First")
s1.dispsd("First")