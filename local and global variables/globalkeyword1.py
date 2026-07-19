#Program to demonstrate Global Keyword
#Ex-1
def modify1():
    global a
    a=a+1
def modify2():
    global a
    a=a*10
#Main Program
a=10
print("Value of 'a' (Global variable) before function call:",a)
modify1()
modify2()
print("Value of 'a' (Global variable) after function call:",a)