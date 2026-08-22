#college.py
from univer import univ
class College(univ):
    def getdata(self):
        self.cname=input("Enter College Name: ")
        self.cloc=input("Enter College Location: ")
        super().getdata()
    def dispdata(self):
        print("--------------------------------------------")
        print("College Details")
        print("--------------------------------------------")
        print("\tCollege Name:", self.cname)
        print("\tCollege Location:", self.cloc)
        print("--------------------------------------------")