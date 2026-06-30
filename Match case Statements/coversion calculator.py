#program to perform all the conversions by using match case statements
#Ex-4
s="""
===================================================
	 Base Conversion calculator
===================================================
        1.	Dec  to Bin------------bin()
            Dec to Oct-------------oct()
            Dec to Hex------------hex()

        2.	Bin to Dec------------Automatic
            Bin to Oct------------oct()
            Bin to Hex------------hex()

        3.    Oct to Dec-------------Automatic
            Oct to Bin-------------bin()
            Oct to Hex------------hex()						

        4.	Hex to Dec------------Automatic
            Hex to Bin------------bin()
            Hex to Oct------------oct()
===================================================
"""
print(s)
ch=int(input("Enter your choice:"))
match(ch):
    case 1:
        dv=int(input("Enter Integer Value(Dec Number System):"))
        bv=bin(dv)
        ov=oct(dv)
        hv=hex(dv)
        print("\tBin({})={}".format(dv,bv))
        print("\tOct({})={}".format(dv,ov))
        print("\tHex({})={}".format(dv,hv))
    case 2:
        bv=input("Enter Binary Value Preceded with 0b/0B:")
        dv=int(bv,2) # Most IMP
        ov=oct(dv)
        hv=hex(dv)
        print("\tDec({})={}".format(bv,dv))
        print("\tOct({})={}".format(bv,ov))
        print("\tHex({})={}".format(bv,hv))
    case 3:
        ov = input("Enter Octal Value Preceded with 0o/0O:")
        dv = int(ov, 8)  # Most IMP
        bv = bin(dv)
        hv = hex(dv)
        print("\tDec({})={}".format(ov, dv))
        print("\tBin({})={}".format(ov, bv))
        print("\tHex({})={}".format(ov, hv))
    case 4:
        hv = input("Enter Hexa Decimal Value Preceded with 0x/0X:")
        dv = int(hv, 16)  # Most IMP
        bv = bin(dv)
        ov = oct(dv)
        print("\tDec({})={}".format(hv, dv))
        print("\tBin({})={}".format(hv, bv))
        print("\tOct({})={}".format(hv, ov))
    case 5:
        print("Thank you for using this program")
        exit()
    case _:
        print("Invalid choice --try again")