k=input()
l=k.lower()
m=0
n=0
for i in range(len(k)):
    if l.count(l[i])>m:
        m=l.count(l[i])
        n=i
print(k[n])
