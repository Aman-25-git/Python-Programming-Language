#DeadLockOOPEx.py
# Demonstration of Dead lock in OOP

import threading, time
class multable:
    def table(self,n):
        print("=" * 50)
        if (n <= 0):
            print("{}==>{}--> Invali Input".format(threading.current_thread().name, n))
        else:
            for i in range(1, 11):
                print("{} X {} = {}\n".format(n, i, n * i))
                time.sleep(1)
        print("=" * 50)


# main Program
t1 = threading.Thread(target=multable().table, args=(10,))
t2 = threading.Thread(target=multable().table, args=(20,))
t3 = threading.Thread(target=multable().table, args=(-30,))
# Dispatch the sub threads
t1.start()
t2.start()
t3.start()
