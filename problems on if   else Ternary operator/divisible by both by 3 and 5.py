#program to check whether a number is divisible by both 3 and 5 using the if..else operator.
#Ex-17     This checks if the number is divisible by both 3 AND 5
a=int(input("Enter the number:"))

res="Divisible by both 5 and 3" if (a%5)==0 and (a%3)==0 else "Not divisible by both 5 and 3"

print("Entered number is {} that is {}".format(a,res))