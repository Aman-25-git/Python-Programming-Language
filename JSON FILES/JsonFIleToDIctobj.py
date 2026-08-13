#program for Reading JSOIN File Data into Dict Object--json.load()
#JSONFileTODictObj.py
import json
with open("emp.json","r") as fp:
    dictobj = json.load(fp)
    for k,v in dictobj.items():
        print("\t{}---->{}".format(k,v))
    print("--------------------------------------------")