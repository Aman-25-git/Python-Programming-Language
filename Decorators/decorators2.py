#program to demonstrate decorators used in  oops-model-2
#Ex-3

def square(gv):
    def cal():
        n=gv()
        res=n**2
        return n,res
    return cal # we are returning the function name not normal variable

@square         #Internally pvm takes like this square(getval)

def getval():
    return float(input("Enter a number:"))
#Main program
n,res=getval()  #Normal fun call
print("Square({}):{}".format(n,res))

