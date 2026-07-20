#program to demonstrate generator function
#Ex-2
def disp():
    yield "Hello, Bhai!!!"
    yield 67
    yield True
    yield 8-9j
x=disp()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

