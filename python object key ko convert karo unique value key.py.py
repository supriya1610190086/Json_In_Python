import json

# python object key

python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'

# convert unique value key access

json_obj = json.loads(python_obj)
print(json_obj) 


