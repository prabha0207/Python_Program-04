x,y=input().split()
c=[]
c=input().split()
d=c[-int(b):]
e=''
for i in range(len(d)):
    e+=d[i]+" "
for i in range(len(c)-len(d)):
    e+=c[i]+" "
print(e)
