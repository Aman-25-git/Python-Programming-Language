#PolyEx7.py
#PolyEx6.py
#PolyEx5.py
class Circle:
    def __init__(self): # original Constructor
        self.r=float(input("Enter the radius of Circle: "))
        self.ac=3.14*self.r**2
        print("Area of circle:",self.ac)
        print("=============================")
class Square(Circle): # Overridden Constructor

    def __init__(self):
        self.s=float(input("Enter the side of square: "))
        self.sa=self.s*self.s
        print("Area of Square:",self.sa)
        print("=============================")
        super().__init__()

class Rectangle(Square): # Overridden Constructor

    def __init__(self):
        self.l=float(input("Enter the Length of rectangle: "))
        self.b=float(input("Enter the Width of rectangle: "))
        self.ra=self.l*self.b
        print("Area of Rectangle:",self.ra)
        print("=============================")
        super().__init__()


#Main Program
a=Rectangle()
