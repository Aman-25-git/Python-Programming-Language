#Program to read input form keyboard and save that data into file of secondary memory
#StudPickleEx.py
import pickle
def studdata():
    with open("Stud.pickle","ab") as fp:
        while(1):
            sno=int(input("Enter Student ID:"))
            sname=input("Enter Student Name:")
            smarks=float(input("Enter Student Marks:"))
            lst=list()
            lst.append(sno)
            lst.append(sname)
            lst.append(smarks)
            pickle.dump(lst,fp)
            ch=input("Do you want to continue?(y/n):")
            if ch.lower()=="n":
                break
    print("We Succesfully Saved Student Data")

#Main Program
studdata()