import json

# python object

DATA={"Name":"David",
       "class":"I","Age":6
       }

# convert to json data

out_file=open("my.json","w")
json.dump(DATA,out_file,indent=4)
out_file.close()
