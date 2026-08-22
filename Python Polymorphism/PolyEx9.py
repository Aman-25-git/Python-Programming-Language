#PolyEx9.py
class Circle:
    def __init__(self,r): # original Constructor

        self.ac=3.14*r**2
        print("Area of circle:",self.ac)
        print("=============================")
class Square: # Overridden Constructor

    def __init__(self,s):
        self.sa=s*s
        print("Area of Square:",self.sa)
        print("=============================")


class Rectangle(Square,Circle): # Overridden Constructor

    def __init__(self,l,b):

        self.ra=l*b
        print("Area of Rectangle:",self.ra)
        print("=============================")
        Square.__init__(self,float(input("Enter the side of square: ")))    #Class name Apporach
        Circle.__init__(self,float(input("Enter the radius of Circle: ")))    #Class name Apporach


#Main Program
l=float(input("Enter the Length of rectangle: "))
b=float(input("Enter the Width of rectangle: "))
a=Rectangle(l,b)