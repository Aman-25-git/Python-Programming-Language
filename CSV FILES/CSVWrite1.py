#writing data to csv file
#CSVWrite1.py
import csv #Step-1
hn=["Eno","Name","Salary"]  #Step-2
records=[[1,"shiva",234],
         [2,"shiva",235],
         [3,"shiva",236],
         [4,"shiva",237]]   #Step-3
with open("C:\\Users\\USER\\Documents\\Temp\\Employee.csv","w") as fp:  #Step-5
    csvwr=csv.writer(fp) #Step-5
    # Here csvwr object, we have Two Functions: 1. writerow() 2. writerows()
    # write the Header names
    csvwr.writerow(hn)  #Step-6
    # write the Records
    csvwr.writerows(records)    #Step-7
    print("File created --verify")