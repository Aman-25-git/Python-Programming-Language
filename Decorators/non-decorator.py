#Program for Demonstrating with Non-Decorators (Normal Functions)
#Ex-1
def getval():
    return 5
def square():
    n=getval()
    res=n**2
    print("Square({}):{}".format(n,res))
def squareroot():
    n=getval()
    res=n**0.5
    print("SquareRoot({}):{}".format(n,res))
def cube():
    n=getval()
    res=n**3
    print("Cube({}):{}".format(n,res))
#Main Program
square()
squareroot()
cube()