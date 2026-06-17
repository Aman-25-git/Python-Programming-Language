#Program on swapping of any two values with assignment operators
a,b=input("Enter  first value:"),input("Enter second value:")
print("="*56)
print("Original value of first:{}".format(a))
print("Original value of second:{}".format(b))
print("="*56)
#swapping logic
a,b=b,a
print("Swapped value of first:{}".format(a))
print("Swapped value of second:{}".format(b))
print("="*56)
