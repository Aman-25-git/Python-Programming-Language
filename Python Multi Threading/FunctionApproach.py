#FunctionApproach.py
import threading
def fun(var):
    print("{}=>,Welcome To Multi Threading".format(var))

#Main Progarm
fun("SAMANTHA")
print("Thread:{}".format(threading.current_thread().name))