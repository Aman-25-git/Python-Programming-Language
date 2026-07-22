#sbi.py<-----File name also called as module name
bname="States Bank Of India"
brname="himayathnagar"
def simpleint():
    p=float(input("Enter principle amount:"))
    t=float(input("Enter time:"))
    r=float(input("Enter rate of interest:"))
    res=(p*t*r)/100
    totamt=p+res
    print("*"*50)
    print("\tResults of Simple Interest")
    print("*"*50)
    print("Priciple Amount:",p)
    print("Time:",t)
    print("Rate of Interest:",r)
    print("Simple Interest:",res)
    print("\tTotal Amount to pay:",totamt)
    print("*"*50)