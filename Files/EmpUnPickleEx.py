#Program to read the multiple values from file of secondaray memory to object of main memory
#EmpUnPickleEx.py
import pickle
def unpick():
    with open("Emp,pickle","rb") as fp:
        while(1):
            try:
                record = pickle.load(fp)
                for val in record:
                    print(val,end="\t")
                print()
            except EOFError:
                print("End Of File Occured")
                break
#Main Program
unpick()
