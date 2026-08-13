import pickle
def updateEmployee():
    # get all the records for Viewing single Employee Deatils Based on ENO
    records = []  # Outer List
    with open("EmpProject.data", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # Get the Records
    print("-"*50)
    found = False
    empno = int(input("Enter the Employee Number to Update Salary:"))
    for index in range(len(records)):
        if(records[index][0] == empno):
            recindex = index
            found = True
            break
    if(found):
        newsal = float(input("Enter the New Salary:"))
        records[recindex][2] = newsal
        # Re-write Modified Records to the File
        with open("EmpProject.data", "wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("\tEmployee Salary Updated--verify")
    else:
        print("\tEmployee Number Not Found")
    print("-" * 50)

