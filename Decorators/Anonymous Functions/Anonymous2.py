#Program on  whether given str is palindrome or not using lambda (or) Anonymous Functions
#Ex-2
pal=lambda val:"Palidrome" if val==val[::-1] else "Not Palidrome"
#main Program
val=input("Enter any word:")
x1=pal(val)
print("{} is {}".format(val,x1))