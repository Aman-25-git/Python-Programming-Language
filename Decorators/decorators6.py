#Program for accepting a Line of Text and and convert into Both Lower and Upper by using decorators
#without using pre-defined functions
#Ex-7

def lowerconvert(vals):
    def conversion():
        n, uc = vals()
        lc=""
        for ch in n:
            if ord(ch) in range(65,91):
                lc=lc+chr(ord(ch)+32)
            else:
                lc=lc+ch
        return n,uc,lc
    return conversion

def upperconvert(val):
    def covert():
        n=val()
        uc=""
        for ch in n:
            if ord(ch) in range(97,123):
                uc=uc+chr(ord(ch)-32)
            else:
                uc=uc+ch
        return n,uc
    return covert

@lowerconvert       # Internally Pvm do this lowerconvert(upperconvert(getline()))
@upperconvert       # Internally Pvm do this upperconvert(getline())
def getline():
    return input("Enter The Text of line:")

#Main Program
n,uc,lc=getline()
print("Given Text:{}".format(n)) #Normal Function call
print("Upper:{}".format(uc))
print("Lower:{}".format(lc))