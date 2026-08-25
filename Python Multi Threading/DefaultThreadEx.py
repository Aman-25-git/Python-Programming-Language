#Program for Showing Default Therad Name
#DefaultThreadEx.py
import threading
tname=threading.current_thread().name
print("Default Thread Name:",tname)
print("No of Threads:",threading.active_count())