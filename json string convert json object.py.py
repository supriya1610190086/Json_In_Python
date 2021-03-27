import json

# json data 
data='{"Name":"ram","class":"IV","Age":9}'

# convert to python object
res=json.loads(data)
# print(type(res))
print(res)
print(type(res))