#Program to read the multiple values from file of secondaray memory to object of main memory
#StudUnPickleEx.py
import pickle
def unpick():
    with open("Stud.pickle","rb") as fp:
        while(1):
            try:
                record=pickle.load(fp)
                for val in record:
                    print(val,end=" ")
                print()
            except EOFError:
                print("End Of File Occured")
                break
#Main Program
unpick()