#JoinFunsEx.py
import threading,time
def welcome(name):
	print("\t{}-->Hi: {}, Welcome Multi Therading".format(threading.current_thread().name,name))
	print("\t{}-->Going to Sleep for 8 Secs ".format(threading.current_thread().name))
	time.sleep(8)
	print("\t{}-->Coming out-off  Sleep after 8 Secs ".format(threading.current_thread().name))

#Main Program
#Create a Sub Thread
print("Program Execution Started:",threading.current_thread().name)
print("\tInitially,Total Number of Threads=",threading.active_count())  # 1
t1=threading.Thread(target=welcome,args=("Ramulamma",))
print("\tExecution Status of t1 before start()=",t1.is_alive())
t1.start()
print("\tNow,Total Number of Threads=",threading.active_count()) # 2
print("\tExecution Status of t1 after start()=",t1.is_alive())
#Make the Sub Threads to Join with MainThread
t1.join()
print("\tNow,Total Number of Threads=",threading.active_count())
print("\tExecution Status of t1 after Complete Execution/join=",t1.is_alive())
print("Program Execution Ended:",threading.current_thread().name)
