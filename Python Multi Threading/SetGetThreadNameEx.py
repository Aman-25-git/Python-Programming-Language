#program for Showing the Setting the Name  and Getting  name of sub thread
#SetGetThreadNameEx.py
import threading
def welcome(name):
	print("\t{}-->Hi: {}, Welcome Multi Therading".format(threading.current_thread().name,name))

#Main Program
#Create a Sub Thread
t1=threading.Thread(target=welcome,args=("Trvais",))
print("Default Name of Sub Thread before=",t1.name) # Getter
t1.name="vjw"  #  Setter
print("Default Name of Sub Thread after Setting=",t1.name)
#dispatch the sub thread
t1.start()