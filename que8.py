import json
a=["neelam","programmer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","45","63000"]
e=["name","Designation","age","salary"]
# f=["emp1","emp2","emp3","emp4"]
dic1={}
dic2={}
dic3={}
dic4={}
dic5={}
for i in range(len(a)):
    dic1[e[i]]=a[i]
    dic2[e[i]]=b[i]
    dic3[e[i]]=c[i]
    dic4[e[i]]=d[i]

dic5["emp1"]=dic1
dic5["emp2"]=dic2 
dic5["emp3"]=dic3
dic5["emp4"] =dic4
f=json.dumps(dic5)
print(f)
print(type(f))
with open("que8.json","w")as file:
    json.dump(dic5,file,indent=4)
file.close 



