#program to compare two strings and display whether they are equal or not using the if..else operator.
#Ex-30
a=input("Enter first String:")
b=input("Enter second String:")

res= "Two Strings Are Equal" if  a==b else "Two Strings Are NOT Equal"

print("Entered Strings Are ({},{}):{}".format(a,b,res))