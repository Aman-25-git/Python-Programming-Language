#InheritaceEx1.py
#Single Inheritance
class c1:
    def disp1(self):
        print("Disp1()--displayed")
class c2(c1):
    def disp2(self):
        print("Disp2()--displayed")
#Main Program
o2=c2()
o2.disp1()
o2.disp2()