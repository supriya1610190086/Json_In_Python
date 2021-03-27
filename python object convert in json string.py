import json

# python object

dict1={"Name":"Rajesh", 
     "Class":"V", 
     "Age":11
    }

# python object convert to json string 

dict2=json.dumps(dict1)
print(type(dict2))
print(dict2)
