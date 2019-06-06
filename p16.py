n1=int(input())
n2=[]
n2=input().split()
for i in range(len(n2)):
    if n2.count(n2[i])==1:
        print(n2[i])
        break
