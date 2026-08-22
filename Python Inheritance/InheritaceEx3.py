#InheritaceEx3.py
#Hierarchical Inheritance
class c1:
    def disp1(self):
        print("Disp1()--displayed")
class c2(c1):
    def disp2(self):
        print("Disp2()--displayed")
class c3(c1):
    def disp3(self):
        print("Disp3()--displayed")
#Main Program
o2=c2()
o2.disp1()
o2.disp2()
#o2.disp3()  Gives Attribute Error
o3=c3()
o3.disp1()
#o3.disp2() Gives Attribute Error
o3.disp3()