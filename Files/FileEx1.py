#Program for opening file in "r" mode
#FileEx1.py
try:
    fp=open("Student.data","r")
except FileNotFoundError:
    print("File does not exist")
else:
    print("FIle opened in read mode")
    print("Type of fp=", type(fp))
    print("Is File Closed?=", fp.closed)
finally:
    try:
        fp.close()
    except NameError:
        print("File is not opened--so no need to close!")
    else:
        print("Type of fp=", type(fp))
        print("Is File Closed?=", fp.closed)