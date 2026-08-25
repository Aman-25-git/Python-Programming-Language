#program for Showing the Running the Sub thread with start()
#ObjectOrientedApproachEx2.py
import threading  #Step-1
class Greet:  #Step-2
	def welcome(self,name):   #Step-3
		print("\t{}-->Hi: {}, Welcome Multi Therading".format(threading.current_thread().name,name))

#Main Program
#Create a Sub Thread
t1=threading.Thread(target=Greet().welcome,args=("Trvais",))   #Step-4
#dispatch the sub thread
t1.start()   #Step-5