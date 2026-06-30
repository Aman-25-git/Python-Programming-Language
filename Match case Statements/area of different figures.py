#program to perform  the area of different figures by using match case statements
#Ex-2
s="""
===================================================
	 Areas of Different Figures
===================================================
            C . Circle
            R. Rectangle
            S: Square
            T. Triangle
            E. Exit	
==================================================="""
print(s)
ch=input("Enter u r Choice:")
match(ch):
    case 'C' | 'c':
        r=float(input(("Enter radius of Circle:")))
        ac=(3.14)*r**2
        print("Area of Circle for Radius {} is {}".format(r,ac))
    case 'R'| 'r':
        l,b = float(input(("Enter Length of Rectangle:"))),float(input(("Enter Breadth of Rectangle:")))
        ar = l * b
        print("Area of Rectangle is {}".format(ar))
    case 'S' | 's':
        s = int(input(("Enter Side of Square:")))
        as1 = s ** 2
        print("Area of Square for side {} is {}".format(s, as1))
    case 'T' | 't':
        h, b = float(input(("Enter Height of Triangle:"))), float(input(("Enter Base of  Triangle:")))
        at =0.5 * h * b
        print("Area of Triangle is {}".format(at))
    case 'E' | 'e':
        print("Thank you for Using This Program.")
        exit()
    case _:
        print("U Have Entered an invalid choice --try again")

