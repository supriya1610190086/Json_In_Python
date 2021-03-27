import json 

shopping_dict ={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
    }

out_file = open("myfile.json", "w")

json.dump(shopping_dict, out_file, indent = 6)

out_file.close() 


key=list(shopping_dict.keys())
i=0
sum=0
quantity=int(input("enter the number"))
while i<quantity:
    item=input("enter the key")
    i=i+1



