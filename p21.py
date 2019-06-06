u=[]
v=[]
for i in range(3):
    c,d=input().split()
    u.append(c)
    v.append(d)
if u.count(u[0])==3 or v.count(v[0])==3:
    print("yes")
else:
    print("no")
