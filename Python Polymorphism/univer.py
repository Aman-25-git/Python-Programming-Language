#univer.py<---File Name and Module Name
class univ:
    def getdata(self):
        self.uname=input("Enter University Name:")
        self.location=input("Enter Location:")
    def dispdata(self):
        print("-----------------------")
        print("University details")
        print("------------------------")
        print("University Name:",self.uname)
        print("Location:",self.location)
        print("-----------------------")