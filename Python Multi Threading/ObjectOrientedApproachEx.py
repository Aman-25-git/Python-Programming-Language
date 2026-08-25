#program for Showing the Running the Sub thread with start()
#ObjectOrientedApproachEx.py
import threading  #Step-1
class Greet:  #Step-2
	def welcome(self,name):   #Step-3
		print("\t{}-->Hi: {}, Welcome Multi Therading".format(threading.current_thread().name,name))

#Main Program
go=Greet() #Create an Object of Greet to call Its Instance Method
#Create a Sub Thread
t1=threading.Thread(target=go.welcome,args=("Trvais",))   #Step-4
#dispatch the sub thread
t1.start()   #Step-5