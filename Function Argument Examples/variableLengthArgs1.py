#program to define variableLengthArgs
#Ex-1
def d1(a,b,c,d):
    print(a,b,c,d)
def d2(a,b,c):
    print(a,b,c)
def d3(a,b):
    print(a,b)
def d4(a):
    print(a)
d1(1,2,3,4)# function call by 4 positional args
d2(1,2,3)#3 positional args
d3(1,2)#2 positional args
d4(1)#1 positional args

#it will execute here for similar family of function calls we have differnet function defs and function calls
#so it take too large memory space in Ram