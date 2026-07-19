#program Finding Length of each word in a list
#Ex-2
lst=["PYTHON","JAVA","HYDERABAD","NETHER LANDS","ROSSUM"]
d={val:len(val) for val in lst  }
print(d)