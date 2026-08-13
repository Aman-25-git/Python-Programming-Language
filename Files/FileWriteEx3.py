#program for Saving Iterable Object Data into the file
#FileWriteEx3.py
with open("Student.txt","a") as fp:
    #Take an Iterable Object
    itobj={1:"PYTHON",2:"C",3:"C++",4:"Java"}
    #save the Iterable Object Data into the File
    fp.writelines("\n"+str(itobj)+"\n")
    print("Iterable Object data saved in file--verify")