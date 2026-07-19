#program to demonstrate decorators -model-1
#Ex-2

def square(gv):
    def cal():
        n=gv()
        res=n**2
        return n,res
    return cal # we are returning the function name not normal variable

def getval():
    return float(input("Enter a number:"))
#Main program
cl=square(getval)
n,res=cl()
print("Square({}):{}".format(n,res))

