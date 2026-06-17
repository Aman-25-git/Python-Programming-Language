#program on cash dispense on ATM machine by using single-line assignment operator
withdraw=int(input("Enter the amount you want to withdraw:"))
n500=withdraw//500
withdraw=withdraw%500
n200=withdraw//200
withdraw=withdraw%200
n100=withdraw//100
withdraw=withdraw%100
print("="*59)
print("Number of n500:{}".format(n500))
print("Number of n200:{}".format(n200))
print("Number of n100:{}".format(n100))
print("="*59)
