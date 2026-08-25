#BankTransOOPsEx.py
import threading,time
class bank:
    acbal=2000 #Class level Variable
    L=threading.Lock()  #Class level Variable
    def withdraw(self,wamt):
        bank.L.acquire()
        if(wamt>bank.acbal):
            print("{}-->Hi,{}->Cheque is bounced-contact to source".format(threading.current_thread().name,wamt))
            time.sleep(1)
        else:
            bank.acbal=bank.acbal-wamt
            print("{}-->Hi,{}->Cheque is Cleared".format(threading.current_thread().name, wamt))
            print("NOW ACCBALANCE :{}".format(bank.acbal))
            time.sleep(1)
        bank.L.release()
#main Program
t1=threading.Thread(target=bank().withdraw,args=(1300,))
t1.name="Suresh"
t2=threading.Thread(target=bank().withdraw,args=(500,))
t2.name="Mahesh"
t3=threading.Thread(target=bank().withdraw,args=(5000,))
t3.name="Rajesh"
t4=threading.Thread(target=bank().withdraw,args=(1000,))
t4.name="Ramesh"
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()