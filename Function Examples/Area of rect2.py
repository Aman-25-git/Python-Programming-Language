#program for calculating area of rectangle by function chaining
#Ex-7
def ReadLB():
    L=float(input("Enter the length of the rectangle: "))
    B=float(input("Enter the Breadth of the rectangle: "))
    return L,B

def calArea():
    L,B=ReadLB()# One Function is calling another--Called Function Chain
    ar=L*B
    DispResult(L, B, ar)# One Function is calling another--Called Function Chain

def DispResult(L,B,ar):
    print("-"*50)
    print("\tLength=",L)
    print("\tBreadth=",B)
    print("Area of Rect:",ar)
    print("-"*50)


#main program
calArea()

