#Program to demonstrate the dict comprehension in python
#Ex-1
lst=[10,20,30,-5,-6,60]
dictobj={val:val**2 for val in lst if val>0}
print(dictobj)