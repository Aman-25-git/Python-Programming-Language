#Program on swapping of any two values diff logic using bit wise XOR operator
a,b=int(input("Enter First Value: ")),int(input("Enter Second Value: "))
print("*"*50)
print("\tOriginal Value of a={}".format(a))
print("\tOriginal Value of b={}".format(b))
print("*"*50)
a=a^b
b=a^b
a=a^b
print("\tOriginal Value of a={}".format(a))
print("\tOriginal Value of b={}".format(b))
print("*"*50)
