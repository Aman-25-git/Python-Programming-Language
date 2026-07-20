#Program for Demonstrating Generators Concept
#Ex-5
def amanrange(start,stop,step):
    while(start<=stop):
        yield start
        start=start+step
#Main program
r=amanrange(10,21,2)
print(next(r))
print(next(r))
for i in r:
    print(i)