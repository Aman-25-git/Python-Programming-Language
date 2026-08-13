#Program to demonstrate RAF
#RandomAccesFileEx.py
with open("Student.txt","r") as f:
    print("Intial fp is at:",f.tell())
    filedata=f.read(3)
    print(filedata)
    print("Now fp is at:",f.tell())
    f.seek(0)
    print("Now fp is at:", f.tell())
    filedata = f.read(7)
    print(filedata)
    f.seek(10)
    print("Now fp is at:", f.tell())
