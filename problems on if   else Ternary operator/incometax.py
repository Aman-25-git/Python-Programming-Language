#program to determine whether an entered salary qualifies for income tax based on a specified threshold using the if..else operator.
#Ex-27
a=float(input("ENTER YOUR SALARY:"))

res= "You are Qualifies for income Tax" if a>=1200000  else "You are NOT Qualifies for income Tax"

print("Your Salary is {} That is {}".format(a,res))

