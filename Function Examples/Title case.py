#program for accepting a Line fo Text and convert it into Title Case
# (Don't use title())
# Ex-9
def readline():
    return input("Enter Line of Text:")
def Amantitle():
    line=readline() # One Function Calls another Function--Function Cahin

    words=line.split()
    tc=""
    for word in words:
        tc=tc+" "+word[0].upper()+word[1:].lower()
    else:
        print(tc)
#Main Program
Amantitle()