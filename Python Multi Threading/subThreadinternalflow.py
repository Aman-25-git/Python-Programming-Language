#Program for Showing Internal Flow of Sub Threads  along with Default Thread -MainThread
#SubThreadsInternalFlow.py
import threading
def welcome():
    print("Welcome() Executed By:",threading.current_thread().name)
def hello():
    print("Hello() Executed By:",threading.current_thread().name)
def bye():
    print("Bye() Executed By:",threading.current_thread().name)
#Main Program
print("Program Execution Started:",threading.current_thread().name)
#Creating three sub threads for executing three functions
t1=threading.Thread(target=welcome) #Here t1 is  Called Sub Thread Object whose default name is thread-1
t2=threading.Thread(target=hello)   #Here t2 is  Called Sub Thread Object whose default name is thread-2
t3=threading.Thread(target=bye) #Here t3 is  Called Sub Thread Object whose default name is thread-3
#Dispatching the sub threads
t1.start()
t2.start()
t3.start()
#Joining the threads
t1.join()
t2.join()
t3.join()
print("Program Execution Finished:",threading.current_thread().name)