import json
filename = 'text.txt'
mydict = {} 
with open(filename) as fh: 
    for line in fh:
        key, value= line.strip().split(None, 1)
        print(key,value)
        mydict[key] = value
out_file = open("text_file.json", "w") 
json.dump(mydict, out_file) 
out_file.close()
 