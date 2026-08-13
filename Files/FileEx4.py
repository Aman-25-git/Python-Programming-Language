#Program to open file in "r" mode
#FileEx4.py
try:
    with open("student1.data","r") as fp:
        print("FIle opened in read mode")
        print("Type of fp=", type(fp))
        print("Is File Closed?=", fp.closed)
except FileNotFoundError:
    print("File not found error")
except NameError:
    print("File is not opened--so no need to close!")
