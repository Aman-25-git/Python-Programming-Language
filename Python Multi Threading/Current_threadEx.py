#Current_threadEx.py
#program for Getting  Currently Executing Thread
import threading
t=threading.current_thread()
print("The Thraed Name :{}".format(t))
print("-"*60)
print("Default Thread Name:{}".format(threading.current_thread().name))
