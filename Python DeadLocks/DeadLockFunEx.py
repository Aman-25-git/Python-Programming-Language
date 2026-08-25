#Demonstration of Dead lock
#DeadLockFunEx.py
import threading,time
def table(n):
    print("="*50)
    if(n<=0):
        print("{}==>{}--> Invali Input".format(threading.current_thread().name,n))
    else:
        for i in range(1,11):
            print("{} X {} = {}".format(n,i,n*i))
            time.sleep(1)
    print("="*50)
#main Program
t1=threading.Thread(target=table,args=(10,))
t2=threading.Thread(target=table,args=(20,))
t3=threading.Thread(target=table,args=(-30,))
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
    