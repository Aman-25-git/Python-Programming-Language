#Program on Simple Interest using if  else statement
#Ex-3
p=float(input("Enter Principle amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
if(p>0) and (t>0) and (r>0):
    si=(p*t*r)/100
    print("*"*50)
    print("Results of Simple Interest")
    print("*"*50)
    print("Principle Amount:{}".format(p))
    print("Time:{}".format(t))
    print("Rate of Interest:{}".format(r))
    print("Simple Interest:{}".format(si))
    print("*"*50)
else:
    if(p<=0):
        print("{} is Invalid Principle amount".format(p))
    if(t<=0):
        print("{} is Invalid Time".format(t))
    if(r<=0):
        print("{} is Invalid Rate of interest".format(r))

print("Execution of program is completed!!@$!!!")