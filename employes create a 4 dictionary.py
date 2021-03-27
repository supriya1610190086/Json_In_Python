import json

values_1=["neelam","programer","24","2400"]
keys=["name","Designation","Age","salary"]
employes1={}
employes2={}
employes3={}
employes4={}
dict1={}

i=0
while i<len(values_1):
    keys1=keys[i]
    j=0
    while j<len(keys):
        employes1[keys[j]]=values_1[j]
        j=j+1
    i=i+1

dict1["employes1"]=employes1

values_2=["komal","trainer","24","20000"]
k=0
while k<len(values_2):
    keys_2=keys[k]
    l=0
    while l<len(keys):
        employes2[keys[l]]=values_2[l]
        l=l+1
    k=k+1

dict1["employes2"]=employes1

values_3=["anuradha","HR","25","40000"]
m=0
while m<len(values_3):
    keys_3=keys[m]
    n=0
    while n<len(keys):
        employes3[keys[n]]=values_3[n]
        n=n+1
    m=m+1

dict1["employes3"]=employes3

values_4=["Abhishek","manager","29","63000"]  
o=0
while o<len(values_4):
    keys_4=keys[o]
    p=0
    while p<len(keys):
        employes4[keys[p]]=values_4[p]
        p=p+1
    o=o+1

dict1["employes4"]=employes4

import json

file =json.dumps(dict1)
print(file)


