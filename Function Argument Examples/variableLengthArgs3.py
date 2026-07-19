#program to define variableLengthArgs
#Ex-3
def d(a,b,c,d):
    print(a,b,c,d)
d(1,2,3,4)# function call by 4 positional args
def d(a,b,c):
    print(a,b,c)
d(1,2,3)#3 positional args
def d(a,b):
    print(a,b)
d(1,2)#2 positional args
def d(a):
    print(a)
d(1)#1 positional args
#This is going to execute Because we have defined
#the fuction definition first and after that we have
#declared function call for that particular fun definition
#so that is reason it is going to execute
#But We have one limitation i.e, if we have 1000 functions calls of similar familiy
#then we have to declare 1000 function definitions that leads to more
#development time so inorder to overcome this we are using Pure Variable Length Args concept

