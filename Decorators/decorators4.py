#Program for Cal Square, Square root and cube  of a Given Number By using Decorator--Model-2
#Ex-5
def cube(crt):
    def processcube():
        n,sqv,sqrv=crt()
        cbv=n**3
        return n,sqv,sqrv,cbv
    return processcube

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

@cube       #Internally pvm takes like this cube(squareroot(square(getval)))
@squareroot #Internally pvm takes like this squareroot(square(getval))
@square     #Internally pvm takes like this square(getval)
def getval():
    return float(input("Enter a number: "))

#Main Program
n,sqv,sqrv,cbv=getval()
print("Square({}):{}".format(n,sqv))
print("SquareRoot({}):{}".format(n,sqrv))
print("Cube({}):{}".format(n,cbv))
