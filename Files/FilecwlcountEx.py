#Program to count the lines,words,char's of file content
#FilewlcountEx.py
def countLines():
    filename=input("Enter a file name:")
    with open(filename,"r") as fp:
        nl=0
        nw=0
        nc=0
        for line in fp:
            nl=nl+1
            nw=nw+len(line.split())
            nc=nc+len(line)
        else:
            print("Number of lines in the file: ",nl)
            print("Number of words in the file: ",nw)
            print("Number of characters in the file: ",nc)
    print("Done")

#Main Program
countLines()