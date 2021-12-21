import json
a={"name":"anjali","age":20,"class":"third_year"}
b=json.dumps(a)
print(b)
print(type(b))
print(type(a))