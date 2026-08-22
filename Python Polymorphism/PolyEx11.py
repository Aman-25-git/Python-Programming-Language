#PolyEx11.py
class univer:
    def getdata(self):
        self.uname=input("Enter your university  name: ")
        self.loc=input("Enter your location: ")
    def dispdata(self):
        print("----------------------------------------")
        print("\tUniversity Details")
        print("-----------------------------------------")
        print("University Name:",self.uname)
        print("Location:",self.loc)
        print("------------------------------------------")

class college(univer):
    def getdata(self):
        self.cname=input("Enter your college name: ")
        self.cloc=input("Enter your college location: ")
        super().getdata()
    def dispdata(self):
        print("-"*50)
        print("\tCollege Details")
        print("-"*50)
        print("College Name:",self.cname)
        print("College Location:",self.cloc)
        print("-"*50)
class Student(college):
    def getdata(self):
        self.sno=input("Enter Student Number: ")
        self.sname=input("Enter  Student Name: ")
        self.sloc=input("Enter  Student Location: ")
        self.crs=input("Enter  Student Course: ")
        super().getdata()
    def dispdata(self):
        univer.dispdata(self)
        college.dispdata(self)
        print("-"*50)
        print("Student Details")
        print("-"*50)
        print("Student Number:",self.sno)
        print("Student Name:",self.sname)
        print("Student Location:",self.sloc)
        print("Student Course:",self.crs)
        print("-"*50)

#Main Program
s=Student()
s.getdata()
s.dispdata()
