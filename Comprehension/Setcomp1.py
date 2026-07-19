#Program to demonstrate the Set comprehension in python
#Ex-1
lst=[1,2,34,5,90,-9,-8,-6,-56,45]
setobj={val for val in lst if val>0}
print(setobj)
setobj1={val for val in lst if val<0}
print(setobj1)