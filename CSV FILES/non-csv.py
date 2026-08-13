#reading data without csv module
#non-csv.py
print("----------------------------------------")
with open("C:\\Users\\USER\\Documents\\Temp\\Student.csv","r") as fp:
    csvdata=fp.read()
    print(csvdata)
print("---------------------------------------")