#Program to print 1 as one etc upto 9 as nine
#Ex-2
val=int(input("Enter Any Number(or)Digit:"))
if(val==0):
    print("{} is ZERO ".format(val))
elif(val==1):
    print("{} is ONE ".format(val))
elif(val==2):
    print("{} is TWO ".format(val))
elif(val==3):
    print("{} is THREE ".format(val))
elif(val==4):
    print("{} is FOUR ".format(val))
elif(val==5):
    print("{} is FIVE ".format(val))
elif(val==6):
    print("{} is SIX ".format(val))
elif(val==7):
    print("{} is SEVEN ".format(val))
elif(val==8):
    print("{} is EIGHT ".format(val))
elif(val==9):
    print("{} is NINE ".format(val))
elif(val<=0) and val in range(-1,-10,-1):
    print("{} is -Ve DIGIT ".format(val))
elif(val<=10) and val not in range(-9,10,1):
    print("{} is -ve NUMBER ".format(val))
elif(val>=10) and val not in range(-1,-10,-1):
    print("{} is +Ve NUMBER ".format(val))

print("HURRY U HAVE  EXECUTED THE PROGRAM SUCCESSFULLY")
