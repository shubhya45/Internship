t1=(0,8,4,6,5,7,8,2,3,4)
l=[]
for i in range (len(t1)):
    count=t1.count(t1[i])
    if count >1 and t1[i] not in l:
      l.append(t1[i])
      print(t1.count(i))
     
     
print(l)
