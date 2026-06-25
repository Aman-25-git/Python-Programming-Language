#program to check whether a given character is an alphabet or not using the if..else operator
#Ex-14
a=str(input("Enter any character:"))

res="Alphabet" if (a>="a" and  a<='z') or (a>='A'and a<='Z') else "NOT AN ALPHABET"

print("Entered character is {} that is {}".format(a,res))