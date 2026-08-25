#Program for Showing the Execution time of Multiple Sub Threads along with  MainThread
#SubThreadsFlowWithOops2.py
import threading,time
class SqNumbers:
	def __init__(self,lst):
		self.lst=lst
	def  squares(self):
		for val in self.lst:
			print("\t{}-->Square({})={}".format(threading.current_thread().name,val,val**2))
			time.sleep(1)
class CbNumbers:
	def __init__(self,lst):
		self.lst=lst
	def  cubes(self):
		for val in self.lst:
			print("\t{}-->cube({})={}".format(threading.current_thread().name,val,val**3))
			time.sleep(1)
#Main Program
bt=time.time()
print("Program Execution Started:",threading.current_thread().name)
lst=[10,12,4,15,16,17,19,23,24]
#Create a Sub Thread for executing squares()
t1=threading.Thread(target=SqNumbers(lst).squares  )
#Create a Sub Thread for executing cubes()
t2=threading.Thread(target=CbNumbers(lst).cubes )
#Dispatch the sub threads   
t1.start()
t2.start()
#Join the Sub Threads
t1.join()
t2.join()
print("Program Execution Ended:",threading.current_thread().name)
et=time.time()
print("Total Execution Time of Sub Threads=",(et-bt))