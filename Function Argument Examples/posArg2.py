#program to define a positional arguments in python
#Ex-2
def info(sno,sname,marks,city):
    print(sno,sname,marks,city)
#main program
info( 10,"Rossom",98.78,"Madras")
info(20,"Bhaj",90,"Madras")
info(30,"Bhsd",98,"Madras")
info(40,"Bh",90.89,"Madras")
#here for different students having same city so writing
# same city for all is space taking more by os
# so to overcome this we have to use default arguments
# i.e, present in next example
