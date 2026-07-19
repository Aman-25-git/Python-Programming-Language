#Program on swap case concept
#Ex-10
def Readline():
    return input("Enter line of text/word:")
def Amanswapcase():
    lines=Readline()
    sc=""
    for ch in lines:
        if ch.isupper():
            sc=sc+ch.lower()
        elif ch.islower():
            sc=sc+ch.upper()
        else:
            sc=sc+ch
    else:
        print("Swap Case:",sc)
#Main Program
Amanswapcase()