#Program for Copying the content of One into Another File
#FileCopyContentEx.py
def filecopy():
    try:
        srcfile=input("Please enter the source file name:")
        with open(srcfile,"r") as rp:
            dstfile=input("Please enter the destination file name:")
            with open(dstfile,"w") as wp:
                srcfile = rp.read()
                wp.write(srcfile)
                print("1 file is copied")
    except FileNotFoundError:
        print("File Not Found")
    except NameError:
        print("Name Error")

#Main Program
filecopy()