#program to check whether a character is uppercase or lowercase using the if..else operator.
#ex-15
a=str(input("Enter any character:"))

res="UPPER CASE" if (a>="A" and  a<='Z')  else "LOWER CASE" if(a>='a'and a<='z') else "Enter valid character"


print("Entered character is {} that is in {}".format(a,res))