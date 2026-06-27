#Program on given number is +Ve or -Ve or 0
#Ex-2
val=float(input("Enter a number: "))
if(val>0):
    print("\t{} is +ve number".format(val))
else:
    if(val<0):
        print("\t{} is -ve number".format(val))
    else:
        print("\t{} is zero".format(val))
print("Execution of program has been completed!!@@!!")