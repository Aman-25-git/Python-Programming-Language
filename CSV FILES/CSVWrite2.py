#adding data to csv file
#CSVWrite2.py
import csv
try:
    arecord=[[34675,"raska.shiva",56.236],
             [897,"shiva kasi",89.237]]   #Step-3
    with open("C:\\Users\\USER\\Documents\\Temp\\Employee.csv","a") as fp:  #Step-5
        csvwr=csv.writer(fp) #Step-5
        print(type(csvwr))
        csvwr.writerows(arecord)    #Step-7
        print("New records are added successfully  --verify")
except PermissionError:
    print("Fist Close the csv file ")