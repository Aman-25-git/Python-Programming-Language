#DeadLockEliminateOOPEx.py
# Demonstration of Dead lock Elimination in OOP
import threading, time
class multable:
    def table(self,n):
        L.acquire()#Step-2 Locking The Resources (Function/method)
        print("=" * 50)
        if (n <= 0):
            print("{}==>{}--> Invalid Input".format(threading.current_thread().name, n))
        else:
            for i in range(1, 11):
                print("{} X {} = {}".format(n, i, n * i))
                time.sleep(1)
        print("=" * 50)
        L.release()#Step-3 Release the locked function.method

# main Program
L= threading.Lock() #Step-1 Creating the obj of lock class
t1 = threading.Thread(target=multable().table, args=(10,))
t2 = threading.Thread(target=multable().table, args=(20,))
t3 = threading.Thread(target=multable().table, args=(-30,))
# Dispatch the sub threads
t1.start()
t2.start()
t3.start()
