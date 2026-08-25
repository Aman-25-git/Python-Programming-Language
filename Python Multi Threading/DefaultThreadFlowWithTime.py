#DefaultThreadFlowWithTime.py
#Program for Showing the Execution time of Default Thread-MainThread
import threading, time

def square(lst):
    for val in lst:
        print("\t{}-->Square({})={}".format(threading.current_thread().name,val,val**2))
        time.sleep(1)
def cubes(lst):
    for val in lst:
        print("\t{}-->Cubes({})={}".format(threading.current_thread().name,val,val**3))
        time.sleep(1)

#Main Program
bt=time.time()
print("Program Execution started :",threading.current_thread().name)
lst=[1,2,3,4,5,6,7,8,9]
square(lst)#Function call 1
print("-"*40)
cubes(lst)
print("-"*40)
print("Program Execution ended :",threading.current_thread().name)
et=time.time()
print("Total Execution time:",et-bt)
print("-"*40)