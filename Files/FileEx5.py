#Program to open file in "r+" mode
#FileEx5.py
try:
    with open("student.data","r+") as fp:
        print("FIle opened in read mode")
        print("Type of fp=", type(fp))
        print("Is File Closed?=", fp.closed)
        print("Mode of file is:", fp.mode)
        print("Name of file is:", fp.name)
        print("Is file readable?=",fp.readable())
        print("Is file writable?=",fp.writable())
except FileNotFoundError:
    print("File not found error")
except NameError:
    print("File is not opened--so no need to close!")
