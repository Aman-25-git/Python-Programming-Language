#Program to convert Dict data to Json Data
#JsonDataToDIctData.py
import json
jsonfrmt='{"Eno":"123","Name":"Krishna","SAL":"678.98"}'
print("="*90)
print("Json object content:{} Type:{}".format(jsonfrmt,type(jsonfrmt)))
#Coverting json data to dict data
dict=json.loads(jsonfrmt)
print(type(dict))
for k,v in dict.items():
    print(k,v)
print("="*90)