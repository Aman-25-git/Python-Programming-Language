#To Check how many threads are there no.of threads
#ActiveThreads.py
import threading
print("Thread name:{}".format(threading.current_thread().name))
print("Total No Of Threads are:{}".format(threading.active_count()))