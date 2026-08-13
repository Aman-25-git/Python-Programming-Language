#Reading data from csv file by DIctReader()
#CSVRead1.py
import csv
print("----------------------------------------")
with open("C:\\Users\\USER\\Documents\\Temp\\Student.csv","r") as fp:
    csvdata=csv.DictReader(fp)
    print(type(csvdata))
    for record in csvdata:
        for hn,hv in record.items():
            print(hn,hv)
    print()
print("---------------------------------------")