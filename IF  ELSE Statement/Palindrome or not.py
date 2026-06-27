#Program to implement whether given input is palindrome or not palindrome
#Ex-1
value=input("Enter any value:")
if(value==value[::-1]):
    print("\t{} is a palindrome".format(value))
else:
    print("\t{} is not a palindrome".format(value))
print("Execution of Program has been completed!!!!!!!")
