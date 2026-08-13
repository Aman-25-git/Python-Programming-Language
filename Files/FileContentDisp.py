#Program to display the content of any file in our sysytem
#FileContentDisp.py
def dispfilecon():
    try:
        fileopen=input("Please enter the File Name:")
        with open(fileopen,"r") as fp:
            a=fp.read()
            print(a)
    except FileNotFoundError:
        print("File Not Found")

#Main Program
dispfilecon()


