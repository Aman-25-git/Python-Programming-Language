#program to determine whether a person is eligible for a senior citizen discount using the if..else operator.
#Ex-19
age=int(input("Enter Your Age:"))

res="You are eligible for senior citizen Discount" if age>=60 else "You are NOT eligible for senior citizen Discount"

print("You are {} years old, So {}".format(age,res))