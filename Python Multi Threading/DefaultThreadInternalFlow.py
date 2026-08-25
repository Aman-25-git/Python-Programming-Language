#Program for Showing Internal Flow of Default Thread -MainThread
#DefaultThreadInternalFlow.py
import threading
def welcome():
    print("Welcome() Executed By:",threading.current_thread().name)
def hello():
    print("Hello() Executed By:",threading.current_thread().name)
def bye():
    print("Bye() Executed By:",threading.current_thread().name)
#Main Program
print("Program Execution Started:",threading.current_thread().name)
print("-"*50)
welcome()
print("-"*50)
hello()
print("-"*50)
bye()
print("-"*50)
print("Program Execution Started:",threading.current_thread().name)