#Program to demonstrate Global Keyword
#Ex-2
def modify1():
    global a,b
    a=a+1
    b=b+1
def modify2():
    global a,b
    a=a*10
    b=b*10
def accesvals():
    c=a+10
    d=b+10
    print("\tLocal Var C Value:", c)
    print("\tLocal Var D Value:", d)


#Main Program
a,b=10,20
print("Value of 'a' and 'b' (Global variable) before function call:",a,b)
modify1()
modify2()
accesvals()
print("Value of 'a' and 'b' (Global variable) after function call:",a,b)