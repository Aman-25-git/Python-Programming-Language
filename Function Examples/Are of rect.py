#program for calculating area of rectangle
#Ex-6
def ReadLB():
    L=float(input("Enter the length of the rectangle: "))
    B=float(input("Enter the Breadth of the rectangle: "))
    return L,B

def calArea(L,B):
    return L*B


def DispResult(L,B,ar):
    print("-"*50)
    print("\tLength=",L)
    print("\tBreadth=",B)
    print("Area of Rect:",ar)
    print("-"*50)
#main program
L,B=ReadLB()
ar=calArea(L,B)
DispResult(L,B,ar)
