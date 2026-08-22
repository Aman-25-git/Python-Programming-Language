#PolyEx10.py
class Circle:
    def area(self,r): # original Method

        self.ac=3.14*r**2
        print("Area of circle:",self.ac)
        print("=============================")
class Square: # Overridden Method

    def area(self,s):
        self.sa=s*s
        print("Area of Square:",self.sa)
        print("=============================")


class Rectangle(Square,Circle): # Overridden Constructor

    def area(self,l,b):

        self.ra=l*b
        print("Area of Rectangle:",self.ra)
        print("=============================")
        Square.area(self,float(input("Enter the side of square: ")))    #Class name Apporach
        Circle.area(self,float(input("Enter the radius of Circle: ")))    #Class name Apporach


#Main Program
l=float(input("Enter the Length of rectangle: "))
b=float(input("Enter the Width of rectangle: "))
a=Rectangle()
a.area(l,b)