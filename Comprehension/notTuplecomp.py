#NotTupleCompEx.py
#Program for Getting +VE and -VE Values Separetely
lst=[10,-20,30,0,40,-50,-60,70,-80]
pslist=( val  for val in lst  if val>0   ) # It is Not tuple Comprehension
#Here pslist is an object of <class, generator>
#Convert generator object into list /set/tuple
t=tuple(pslist)
print(t,type(t))
'''s=set(pslist)
print(s,type(s))'''