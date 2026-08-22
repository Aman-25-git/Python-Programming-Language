#PolyEx2.py
class Rectangle:
    def draw(self): # Original Method
        print("Drawing Rectangle")
class Circle(Rectangle):
    def draw(self): # Overridden Method
        print("Drawing Circle")
        super().draw()
class Square(Circle):
    def draw(self): # Overridden Method
        print("Drawing Square")
        super().draw()

#Main Program
s=Square()
s.draw()