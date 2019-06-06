x,y=input().split()
z=[]
z=input().split()
a=z[-int(y):]
b=''
for i in range(len(a)):
    b+=a[i]+" "
for i in range(len(z)-len(a)):
    b+=z[i]+" "
print(b)
