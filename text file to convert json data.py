import json

file = open("text.txt","r")
read=file.read()
file.close()

data_1=json.dumps(read,indent=4)

data=open("my.json","w")
g=data.write(data_1)
data.close()
