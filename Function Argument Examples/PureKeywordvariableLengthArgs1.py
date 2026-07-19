#program to define PureKeywordvariableLengthArgs
#Ex-1
def info(**Aman):
    print(Aman)
#Main Program
info(sno=10,sname="RS",mm=56,em=70,cname="PSF") # Function Call-1 with 5 Keyword Arguments
info(tno=100,tname="TR",sub1="PYTHON",sub2="Numpy")# Function Call-2 with 4 Keyword Arguments
info(cid=1000,cname="JH",hb="Drawing") # Function Call-3 with 3 Keyword Arguments
#By this we cn Define only one function definition and by PureKeywordvariableLengthArgs we can give there particular name,no,marks etc
