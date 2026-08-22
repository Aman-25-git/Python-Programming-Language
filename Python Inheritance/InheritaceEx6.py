#InheritaceEx6.py
class Parent:
    def getparentprop(self):
        self.pp=float(input("Enter property of Parent:"))
class Child(Parent):
    def getchildprop(self):
        self.cp=float(input("Enter property of Child:"))
    def Totalprop(self):
        self.getparentprop()
        self.getchildprop()
        self.tp=self.pp+self.cp
        print("--------------------------------------")
        print("\tParent Property=", self.pp)
        print("\tChild Property=", self.cp)
        print("\tTotal Property=", self.tp)
        print("--------------------------------------")


#Main Program
c=Child()
c.Totalprop()
