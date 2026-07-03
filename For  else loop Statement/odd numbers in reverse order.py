#Program for Generating all Odd Numbers In reverse Order within N
#Ex-11
n=int(input("Enter How Many Odd Number u want to Generate with in the Range:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-" * 50)
    print("Odd Numbers from {} to 1".format(n))
    print("-" * 50)
    if(n%2==0):
        n=n-1
    for i in range(n,0,-2):
        print("\t{}".format(i))
    else:
        print("-" * 50)