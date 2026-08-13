#Program for Accepting student details from KBD and save in File as Records
#FileWriteEx2.py
def studentdata():
    with open("Student.txt","w") as fp:
        print("----------------------------------------")
        #taking dynamic input form end user
        rno=int(input("Enter student roll no:"))
        sname=input("Enter student name:")
        smarks=input("Enter student marks:")
        print("----------------------------------------")
        #saving into file
        fp.write(str(rno)+"\t")
        fp.write(sname+"\t")
        fp.write(smarks)
        print("Student Data saved in File-verify")
        print("----------------------------------------")
#Main program
studentdata()

