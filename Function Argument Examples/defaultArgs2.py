#program to define a Default arguments in python
#Ex-2

def info(sno,sname,marks,crs="Madras"):
    print(sno,sname,marks,crs)
#main program
info( 10,"Rossom",98.78)
info(20,"Bhaj",90 )
info(30,"Bhsd",98 )
info(40,"Bh",90.89 )
info(50,"Bhsd",90.89,crs="Khammam" )
#we are not declaring the city in every function call
#we declared it in function definition as default param
#if we want different city for on student
#we can use there keyword arguments like mentioned above
