#program to check whether a number is divisible by 5 using the if..else operator.
#Ex-16
a=int(input("Enter the number:"))

res="Divisible by 5" if a%5==0 else "Not divisible by 5"

print("Entered number is {} that is {}".format(a,res))