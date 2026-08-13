#program for accepring any File Name and display Its Content
#FileContentDisplay.py
def displayfilecontent():
    try:
        filename=input("Enter Any File Name:")
        with open(filename,"r") as fp:
            filedata=fp.read()
            print("-----------------------------------------")
            print(filedata)
            print("-----------------------------------------")
    except FileNotFoundError:
        print("File Does Not Exist")

#Main Program
displayfilecontent()