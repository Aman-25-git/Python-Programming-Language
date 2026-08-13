#Program to demonstrate write()
#FileWriteEx1.py
with open("Student1.data","w") as fp:
    fp.write(str(678)+ "\t")
    fp.write("Aman"+"\t")
    fp.write("56.78"+"\t")
    print("student data Saved in file ---check")