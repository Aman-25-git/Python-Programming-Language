#Program for Demonstrating Generators Concept
#Ex-5
def amanrange(start,stop=1,step=1):
    if(stop<=start):
        stop=start
        start=1
    while(start<=stop):
        yield start
        start=start+step
#Main program
r=amanrange(10)
print(next(r))
print(next(r))
for i in r:
    print(i)
print("------------------------------")
r2=amanrange(10,16) # Here r2' is an object of <class, generator>
#To get the values from generator object, we use next(generator-object)
print(next(r2))
print(next(r2))
for val in r2:
    print("\t{}".format(val))
print("---------------------------------------------------------------")
r3=amanrange(10,21,2) # Here r' is an object of <class, generator>
#To get the values from generator object, we use next(generator-object)
print(next(r3))
print(next(r3))
for val in r3:
    print("\t{}".format(val))
print("---------------------------------------------------------------")
