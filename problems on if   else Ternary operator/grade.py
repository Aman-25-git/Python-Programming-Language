#a program to calculate the grade of a student (A, B, C, or F) using nested if..else operators.
#Ex-8
a=int(input("Enter U R Marks Number:"))

res= "Grade is :F" if a>=0 and a<35 else "Grade is:C" if a>=35 and a<60 else "Grade is:B" if a>=60 and a<85 else "Grade is:A" if a>=85 and a<=100  else "Enter input value in correct way! i.e,+ve number"

print("Entered Marks are {} That is {}".format(a,res))

