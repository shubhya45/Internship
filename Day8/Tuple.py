t=("Tuple","is","awesome")
# length=tuple((len(word) for word in t)) # Comprehensive Method
# print(length)

l=[]
for i in t:
    l.append(len (i))

t2=tuple(l)
print(t2)

