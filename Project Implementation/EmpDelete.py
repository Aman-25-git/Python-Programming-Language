#EmpDelete.py
import pickle
def deleteEmployee():
    # get all the records for Viewing single Employee Details Based on ENO
    records = []  # Outer List
    with open("EmpProject.data", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Get Employee Number for Removing the Record
    print("-"*50)
    found=False
    empno=int(input("Enter Employee Number to Delete:"))
    for record in records:
        if(record[0]==empno):
            rec=record
            found=True
            break
    if(found):
        records.remove(rec)
        #Re-write the Remaining Records to File after delete
        with open("EmpProject.data","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tEmployee Deleted--Verify")
    else:
        print("\tEmployee Number Not Found")
    print("-"*50)
