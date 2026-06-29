#Program to print 1 as one etc upto 9 as nine
#Ex-3
val=int(input("Enter any Number:"))
di={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
print("{} is {}".format(val,di.get(val) if di.get(val)!=None else "-ve digit" if val<0 and val in range(-1,-10,-1) else "-ve NUMBER" if val<-9 else "+ve Number"))