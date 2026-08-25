#FunctionApproch2.py#FunctionApproach.py
import threading
def fun(var):
    print("{}===>{}=>,Welcome To Multi Threading".format(threading.current_thread().name,var))

#Main Progarm
#Creating SubThread
t1=threading.Thread(target=fun,args=("SAMANTHA",))
#dispatching the thread sub
t1.start()
print("\nThread:{}".format(threading.current_thread().name))