#Program for Finding the Sum of Square and Cubes N Natural Nums
#Ex-9
n=int(input("Enter How Many Natual Number Sum u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    s=0
    ss=0
    cs=0
    print("-"*50)
    print("NatNums\t\tSquares\t\tCubes")
    print("-" * 50)
    for i in range(1,n+1):
       print("\t{}\t\t{}\t\t{}".format(i,i**2,i**3))
       s=s+i
       ss=ss+i**2
       cs=cs+i**3
    else:
       print("-" * 50)
       print("\t{}\t\t{}\t\t{}".format(s, ss, cs))
       print("-" * 50)
