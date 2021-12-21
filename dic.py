name=["megha","raghav","pranjali","suman"]
marks=[90,81,82,70]
dict={}
for i in name:
    for j in marks:
        dict[i]=j
        marks.remove(j)
        break
print(dict)