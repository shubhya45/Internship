dict1={'a':1,'b':2,'c':3,'d':1}
dict2={}
for k, v in dict1.items():
    if  v in dict2:
        dict2[v].append(k)
    else:
        dict2[v]=[k]
print(dict2)

