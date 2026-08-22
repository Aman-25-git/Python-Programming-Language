#Non-inheritace.py
class c1:
    def disp1(self):
        print("Disp1()--displayed")
class c2:
    def disp2(self):
        print("Disp2()--displayed")
class c3:
    def disp3(self):
        print("Disp3()--displayed")
#Main Program
o1=c1()
o2=c2()
o3=c3()
o1.disp1()
o2.disp2()
o3.disp3()