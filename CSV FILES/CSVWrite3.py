#adding data to csv file
#CSVWrite3.py
import csv
hnames=["PID","PNAME","PRICE"] #Step-2
records=[{"PID":"p100","PNAME":"KitKat","PRICE":100.25},
         {"PID":"p200","PNAME":"Cadburry","PRICE":50.75},
         {"PID":"p300","PNAME":"ChacoPie","PRICE":25.25},
         {"PID":"p400","PNAME":"MangoByte","PRICE":15.25}]
with open("C:\\Users\\USER\\Documents\\Temp\\Product.csv","w",newline="") as fp:
    csvwr=csv.DictWriter(fp,fieldnames=hnames)
    print(type(csvwr))
    csvwr.writeheader()
    csvwr.writerows(records)    #Step-7
    print("CSV File Created  --Verify")
