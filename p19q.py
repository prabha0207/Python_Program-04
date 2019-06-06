e=int(input())
g=0
h=''
for i in range(2,e+1):
    if e%i==0:
        f=1
        while f<=i:
            if i%f==0:
                g+=1
            f+=1
        if g==2:
            d+=str(i)+" "
        g=0
print(h)
