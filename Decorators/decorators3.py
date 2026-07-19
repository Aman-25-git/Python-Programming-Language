#Program for Cal Square  and Square root of a Given Number By using Decorator--Model-2
#Ex-4
def squareroot(srt):
    def process():
        n,sqv=srt()
        sqrv=n**0.5
        return n,sqv,sqrv
    return process

def square(gv):
    def cal():
        n=gv()
        res=n**2
        return n,res
    return cal

@squareroot #Internally pvm takes like this squareroot(square(getval))
@square     #Internally pvm takes like this square(getval)
def getval():
    return float(input("Enter a number: "))

#Main Program
n,sqv,sqrv=getval()
print("Square({}):{}".format(n,sqv))
print("SquareRoot({}):{}".format(n,sqrv))
