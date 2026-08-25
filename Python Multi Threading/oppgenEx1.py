#program for Generating 1 to N Nubers By using Therads after each and every Second
#OOPGenEx1.py
import threading,time
class Numbers:
	def  generate(self,n):
		print("------------------------------------------------------------")
		if(n<=0):
			print("\t{}---->{} is Invalid Input".format(threading.current_thread().name,n))
		else:
			print("Numbers within :{}".format(n))
			for i in range(1,n+1):
				print("\t{}---->Value :{}".format(threading.current_thread().name,i))
				time.sleep(1)
		print("------------------------------------------------------------")
#main Program
t1=threading.Thread(target=Numbers().generate,args=(int(input("Enter How Many Numbers u want to Generate:")),))
t1.start()