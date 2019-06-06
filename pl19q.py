x=int(input())
c=0
z=''
for i in range(2,x+1):
    if x%i==0:
        b=1
        while b<=i:
            if i%b==0:
                c+=1
            b+=1
        if c==2:
            z+=str(i)+" "
        c=0
print(z)
