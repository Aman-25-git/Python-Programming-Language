#Program on swapping of any two values diff logic
a,b=int(input("Enter  first value:")),int(input("Enter second value:"))
print("="*56)
print("Original value of first:{}".format(a))
print("Original value of second:{}".format(b))
print("="*56)
#swapping logic
a=a*b
b=a//b
a=a//b
print("Swapped value of first:{}".format(a))
print("Swapped value of second:{}".format(b))
print("="*56)
