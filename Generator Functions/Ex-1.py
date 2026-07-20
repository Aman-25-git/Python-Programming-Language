#program to demonstrate generator function
#Ex-1
def disp():
    yield "Hello, Bhai!!!"
x=disp()
print(next(x))