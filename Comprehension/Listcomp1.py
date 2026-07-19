#Program to demonstrate the List comprehension in python
#Ex-1
lst=[10,20,30,-5,-6,60]
pslst=[val for val in lst if val>0]
print(pslst)
nglst=[val for val in lst if val<0]
print(nglst)