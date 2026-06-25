#program to determine whether a business transaction results in profit or loss using the if..else operator.
#Ex-22
a=float(input("Enter the Amount of transaction:"))
b=900
res="Profit" if a>b else "NO PROGIT AND NO LOSS EQUAL" if a==b else "LOSS"
print("Actual cost:{}".format(b))
print("Transaction amount is {} Result is {}".format(a,res))
