k=int(input())
l=input()
m=''
for i in range(-1,-k-1,-1):
    if l[i].lower() not in "aeiou":
        m+=l[i]
print(m)
