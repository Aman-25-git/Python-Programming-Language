#IsAliveFunsEx.py
#program for Showing the Execution Status  of sub thread
import threading
def fun(var):
    print("{}===>{}=>,Welcome To Multi Threading".format(threading.current_thread().name,var))
#Main Progarm
print("Program Execution Started :{}".format(threading.current_thread().name))
#Creating SubThread
t1=threading.Thread(target=fun,args=("SAMANTHA",))
print("Program Execution Status Before Starting The Sub Thread:{}".format(t1.is_alive()))
#dispatching the thread sub
t1.start()
print("Program Execution Status After Starting The Sub Thread:{}".format(t1.is_alive()))
print("\nProgram Execution Completed:{}".format(threading.current_thread().name))