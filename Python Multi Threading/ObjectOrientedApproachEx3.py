#program for Showing the Running the Sub thread with start()
#ObjectOrientedApproachEx3.py
import threading  #Step-1
class Greet:  #Step-2
	def __init__(self,name):
		self.name=name
	def welcome(self):   #Step-3
		print("\t{}-->Hi: {}, Welcome Multi Therading".format(threading.current_thread().name,self.name))

#Main Program
#Create a Sub Thread
t1=threading.Thread(target=Greet("Rossum").welcome)   #Step-4
#dispatch the sub thread
t1.start()   #Step-5