#Program for Demonstrating Generators Concept
#Ex-3

def amanrange(s):
    i=1
    while i<s:
        yield i
        i=i+1
#main Program
r=amanrange(5)
print(next(r))
print(next(r))
print(next(r))
