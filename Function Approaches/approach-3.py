#Program on multiply of two numbers by app-3
#INPUT          :  Taking Input From Function Call(Main Program)
#PROCESS        :  Processing Done in Function Body
#RESULT         :   Result  Displayed in Function Body
#Ex-2
def mul(s,n):
    """This function multiplies two numbers by approach -3"""
    res = s*n
    print("Multiply ({},{}) = {}".format(s, n, res))
s = int(input("Enter A value:"))
n = int(input("Enter B value:"))
mul(s,n)
help(mul)