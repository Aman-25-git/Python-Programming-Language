#PolyEx1.py
#By Using Super()
class Rectangle:
    def draw(self):
        print("Rectangle()--draw")
class Circle(Rectangle):
    def draw(self):
        print("Circle()--draw")
        super().draw()

#Main Program
c=Circle()
c.draw()