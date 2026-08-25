#Program for Showing the Execution time of Multiple Sub Threads along with  MainThread
#SubThreadsFlowWithOops1.py
import threading,time
class Numbers:
	def  squares(self,lst):
		for val in lst:
			print("\t{}-->Square({})={}".format(threading.current_thread().name,val,val**2))
			time.sleep(1)
	def  cubes(self,lst):
		for val in lst:
			print("\t{}-->cube({})={}".format(threading.current_thread().name,val,val**3))
			time.sleep(1)
#Main Program
bt=time.time()
print("Program Execution Started:",threading.current_thread().name)
lst=[10,12,4,15,16,17,19,23,24]
#Create a Sub Thread for executing squares()
t1=threading.Thread(target=Numbers().squares, args=(lst,) )#Here t1 is  Called Sub Thread Object whose default name is thread-1
#Create a Sub Thread for executing cubes()
t2=threading.Thread(target=Numbers().cubes,args=(lst,) )#Here t2 is  Called Sub Thread Object whose default name is thread-2
#Dispatch the sub threads
t1.start()
t2.start()
#Join the Sub Threads
t1.join()
t2.join()
print("Program Execution Ended:",threading.current_thread().name)
et=time.time()
print("Total Execution Time of Sub Threads=",(et-bt))