#program to perform all the Arithmetic operations by using match case statements
#Ex-1
s="""
================================================
    Arithmetic Operations
================================================
        1. Addition
        2. Substraction
        3. Multiplication
        4. Division
        5. Floor Division
        6. Modulo Division
        7. Exponetiation
        8. Exit					
================================================"""
print(s)
ch=int(input("Enter your choice:"))
match(ch):
    case 1:
        print("Enter a,b values for Addition:")
        a,b=float(input()),float(input())
        print("Sum({},{}):{}".format(a,b,a+b))
    case 2:
        print("Enter a,b values for Subtraction:")
        a, b = float(input()), float(input())
        print("Sub({},{}):{}".format(a, b, a - b))
    case 3:
        print("Enter a,b values for Multiplication:")
        a, b = float(input()), float(input())
        print("Mul({},{}):{}".format(a, b, a * b))
    case 4:
        print("Enter a,b values for Division:")
        a, b = float(input()), float(input())
        print("Div({},{}):{}".format(a, b, a / b))
    case 5:
        print("Enter a,b values for Floor Division:")
        a, b = float(input()), float(input())
        print("FDiv({},{}):{}".format(a, b, a // b))
    case 6:
        print("Enter a,b values for Modulo Division:")
        a, b = float(input()), float(input())
        print("MDiv({},{}):{}".format(a, b, a % b))
    case 7:
        print("Enter a,b values for Exponetiation:")
        a, b = float(input()), float(input())
        print("Expo({},{}):{}".format(a, b, a ** b))
    case 8:
        print("Thank you For Using This Program")
        exit()
    case _:
        print("U Have Entered an invalid choice --try again")
