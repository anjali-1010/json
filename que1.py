import json

a='{"Name":"Ram","Class":"IV", "Age":9 }'
d=json.loads(a)
print(d)
print(type(d))
print(type(a))