#program to check whether a given year is a leap year using the if..else operator.
#Ex-12
a=int(input("Enter year:"))

res="LEAP YEAR" if (a%4==0 and a%100!=0) or (a%400)==0  else" NON-LEAP YEAR"

print("Entered year is {} That is {}".format(a,res))