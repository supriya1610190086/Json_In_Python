import json


DATA_python_object= {'4': 5, '6': 7,'1': 3, '2': 4}
print("JSON data:")
res=json.dumps( DATA_python_object , sort_keys=True , indent=4 )
print(res)


