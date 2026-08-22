#InheritaceEx2.py
#Multi-Level Inheritance
class c1:
    def disp1(self):
        print("Disp1()--displayed")
class c2(c1):
    def disp2(self):
        print("Disp2()--displayed")
class c3(c2):
    def disp3(self):
        print("Disp3()--displayed")
#Main Program
o3=c3()
o3.disp1()
o3.disp2()
o3.disp3()