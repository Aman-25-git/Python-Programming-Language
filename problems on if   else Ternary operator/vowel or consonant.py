#program to check whether a character is a vowel or a consonant using the if..else operator.
#Ex-13
a=str(input("Enter any character:"))

res="Vowel" if(str(a)=='a' or 'A' or str(a)=='e'or a=='E' or str(a)=='i'or a=='I' or str(a)=='o'or a=='O' or str(a)=='u'or a=='U') else "Consonant"

print("Entered character is {} that is {}".format(a,res))