u=input()
v=''
for i in u:
    if i=="X":
        v+="A"
    elif i=="Y":
        v+="B"
    elif i=="Z":
        v+="C"
    else:
        v+=chr(ord(i)+3)
print(v)
