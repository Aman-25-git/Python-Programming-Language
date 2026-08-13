#program for Saving Dict object data to the JSON File--json.dump()
#DictDataToJSONFileEx.py
import json
dictobj={'ENO': '100', 'NAME': 'ROSSUM', 'SAL': '12.55'}
with open("emp.json","w") as fp:
    json.dump(dictobj,fp)
    print("Dict data Saved in Json File---Verify")