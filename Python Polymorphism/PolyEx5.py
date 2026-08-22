#PolyEx5.py
class Circle:
    def area(self): # original Method
        self.r=float(input("Enter the radius of Circle: "))
        self.ac=3.14*self.r**2
        print("Area of circle:",self.ac)
        print("=============================")
class Square(Circle): # Overridden Method

    def area(self):
        self.s=float(input("Enter the side of square: "))
        self.sa=self.s*self.s
        print("Area of Square:",self.sa)
        print("=============================")

class Rectangle(Square): # Overridden Method

    def area(self):
        self.l=float(input("Enter the Length of rectangle: "))
        self.b=float(input("Enter the Width of rectangle: "))
        self.ra=self.l*self.b
        print("Area of Rectangle:",self.ra)
        print("=============================")
        Square.area(self)   #Class name Apporach
        Circle.area(self)   #Class name Apporach


#Main Program
a=Rectangle()
a.area()