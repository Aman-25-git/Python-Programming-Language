#InheritaceEx7.py
class GrandParent:
    def getGrandParentProperty(self):
        self.gpp = float(input("Enter Grand Parent Property:"))
class Parent(GrandParent):
    def getParentProperty(self):
        self.pp=float(input("Enter Parent Property:"))
class Child(Parent):
    def getChildProperty(self):
        self.cp=float(input("Enter Child Property:"))
    def totalproperty(self):
        self.tp=self.gpp+self.pp+self.cp
        print("--------------------------------------")
        print("\tGrand Parent Property=", self.gpp)
        print("\tParent Property=",self.pp)
        print("\tChild Property=",self.cp)
        print("\tTotal Property=",self.tp)
        print("--------------------------------------")
#main Program
co=Child()
co.getGrandParentProperty()
co.getParentProperty()
co.getChildProperty()
co.totalproperty()