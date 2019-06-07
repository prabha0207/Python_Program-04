u=input()
v=[]
w=''
for i in u:
    v.append(i)
v.reverse()
for i in v:
    w=w+i
if (u==w):
    print("yes")
else:
    print("no")
