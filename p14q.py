i=int(input())
j=input()
ck=''
for i in range(-1,-i-1,-1):
    if j[i].lower() not in "aeiou":
        k+=j[i]
print(k)
