#Program on multiply of two numbers by app-2
#INPUT          :  Taking Input From Function Body
#PROCESS        :  Processing Done in Function Body
#RESULT         :  Result  Displayed in Function Body
#Ex-2
def mul():
    """This function multiplies two numbers by approach -2"""
    s = int(input("Enter A value:"))
    n = int(input("Enter B value:"))
    res = s*n
    print("Multiply ({},{}) = {}".format(s, n, res))
mul()
help(mul)