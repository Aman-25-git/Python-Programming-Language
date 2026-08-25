#program for accepting a Line of Text and Display Every Word  By using Therads after each and every Second
#WordsGenOOPEx1.py
import threading,time
class Line:
	def gettline(self):
		self.line=input("Enter a Line of Text:")
	def  generate(self):
		print("------------------------------------------------------------")
		self.gettline()
		print("Given Line of Text:",self.line)
		words=self.line.split()
		for word in words:
			print("\t{}".format(word))
			time.sleep(1)
		print("------------------------------------------------------------")
#main Program
t1=threading.Thread(target=Line().generate)
t1.start()