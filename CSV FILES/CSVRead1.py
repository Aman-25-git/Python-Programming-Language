#Reading data from csv file
#CSVRead1.py
import csv
print("----------------------------------------")
with open("C:\\Users\\USER\\Documents\\Temp\\Student.csv","r") as fp:
    csvdata=csv.reader(fp)
    print(type(csvdata))
    for record in csvdata:
        for val in record:
            print(val)
    print()
print("---------------------------------------")