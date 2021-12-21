import json
user1=input("enter a item name")
user2=int(input("how many items"))
shopping={ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}
file=open("que9.json","w")
data=json.dump(shopping,file,indent=4) 
print(type(data))

