#Program on multiply of two numbers by app-4
#INPUT          :  Taking Input From Function Body
#PROCESS        :  Processing Done in Function Body
#RESULT         :   Result  Displayed in Function Call(Main Program)
#Ex-2
def mul():
    """This function multiplies two numbers by approach -4"""
    s = int(input("Enter A value:"))
    n = int(input("Enter B value:"))
    res = s*n
    return s,n,res
a,b,c=mul()
print("Multiply ({},{}) = {}".format(a, b, c))

print("------------------OR-----------------------")

re=mul()# here result is stored in tuple object why means we can't change the coming values
print("Multiply ({},{}) = {}".format(re[0], re[1], re[2]))
print(type(re))
help(mul)