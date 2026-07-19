#Program on multiply of two numbers by app-1
#INPUT          :  Taking Input From Function Call (Main Program)
#PROCESS        :  Processing Done in Function Body
#RESULT         :  Result Given Back to Function Call (Main Program)
#Ex-2
def mul(a,b):
    """This function multiplies two numbers by approach -1"""
    c=a*b
    return c
s=int(input("Enter A value:"))
n=int(input("Enter B value:"))
res=mul(s,n)
print("Multiply ({},{}) = {}".format(s,n,res))