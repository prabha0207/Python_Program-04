u=int(input())
v=[]
x=0
z=0
for i in range(u):
    w=input()
    v.append(w)
for i in v:
    for y in i:
        x+=ord(y)
    if x==612:
        z+=1
    x=0
print(z)
