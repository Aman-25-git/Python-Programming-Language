#program to perform  the Temperature Conversions by using match case statements
#Ex-3
s="""
===================================================
	 Temperature Conversion Scale
===================================================
            1. Fahrenheit to Celcius
            2. Fahrenheit to Kelvin
            3. Celcius to Fahrenheit
            4. Celcius to Kelvin
            5. Kelvin to Fahrenheit
            6. Kelvin to Celcius
            7. Exit
===================================================
"""
print(s)
ch=int(input("Enter your choice:"))
match(ch):
    case 1:
        fah=float(input("Enter Temperature in Fahrenheit:"))
        cel= (fah-32)*(5/9)
        print("The Temperature in {} Fahrenheit is Converted into {} Celcius".format(fah,cel))
    case 2:
        fah = float(input("Enter Temperature in Fahrenheit:"))
        kel = (fah-32)* (5/9) + 273.15
        print("The Temperature in {} Fahrenheit is Converted into {} Kelvin".format(fah, kel))
    case 3:
        cel = float(input("Enter Temperature in Celcius:"))
        fah = cel*(9/5) + 32
        print("The Temperature in {} Celcius is Converted into {} Fahrenheit".format(cel, fah))

    case 4:
        cel = float(input("Enter Temperature in Celcius:"))
        Kel = cel + 273.15
        print("The Temperature in {} Celcius is Converted into {} Kelvin".format(cel, kel))

    case 5:
        kel = float(input("Enter Temperature in Kelvin:"))
        fah =(kel-273.15) (9/5) + 32
        print("The Temperature in {} Kelvin is Converted into {} Fahrenheit".format(kel, fah))
    case 6:
        kel = float(input("Enter Temperature in Kelvin:"))
        cel = kel - 273.15
        print("The Temperature in {} Kelvin is Converted into {} Celsius".format(kel, cel))

    case 7:
        print("Thank you For Using This Program")
        exit()
    case _:
        print("U Have Entered an invalid choice --try again")
