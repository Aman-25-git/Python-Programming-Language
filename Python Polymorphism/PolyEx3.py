#PolyEx3.py
class Rectangle:
    def draw(self): # Original Method
        print("Drawing Rectangle")
class Circle(Rectangle):
    def draw(self): # Overridden Method
        print("Drawing Circle")
        Rectangle().draw()
class Square(Circle):
    def draw(self): # Overridden Method
        print("Drawing Square")
        Circle().draw()

#Main Program
s=Square()
s.draw()