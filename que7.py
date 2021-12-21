import json
a={"Name": "Abhishek","Designation": "CEO of navgurukul","Gender":"male","Age": 29}
file=open("texttt.json","w")
data=json.dump(a,file,indent=4) 
print(type(data))

