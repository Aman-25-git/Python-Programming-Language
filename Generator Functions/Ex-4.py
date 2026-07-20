#Program for Demonstrating Generators Concept
#Ex-4
def amanrange(start,stop):
    while(start<=stop):
        yield start
        start=start+1
#Main program
r=amanrange(10,21)
print(next(r))
print(next(r))
for i in r:
    print(i)