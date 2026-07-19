#program to define variableLengthArgs
#Ex-2
def d(a,b,c,d):
    print(a,b,c,d)
def d(a,b,c):
    print(a,b,c)
def d(a,b):
    print(a,b)
def d(a):
    print(a)
d(1,2,3,4)# function call by 4 positional args
d(1,2,3)#3 positional args
d(1,2)#2 positional args
d(1)#1 positional args
#This will not going to execute any more
# because the function definitions is going to
# update in every function definition so it is not
# going to execute it throws Type Error
# for this problem we have a solution in variableLengthArgs3.py

