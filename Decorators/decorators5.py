#Program for accepting a Line of Text and and convert into Both Lower and Upper by using decorators
#Ex-6

def lowerconvert(vals):
    def conversion():
        n,uc=vals()
        lc=n.lower()
        return n,uc,lc
    return conversion

def upperconvert(val):
    def covert():
        n=val()
        uc=n.upper()
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