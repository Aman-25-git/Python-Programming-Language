#program to check whether a given number is greater than 100 using the if..else operator.
#Ex-26
a=float(input("Enter the number:"))

res="Greater than 100" if a>100 else "Equal Which is not >(or)< 100" if a==100 else "Not Greater than 100"

print("Entered number is {} that is {}".format(a,res))