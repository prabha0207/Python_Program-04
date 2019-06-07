val1=list(map(str,input()))
val2=list(map(str,input()))
for i in range(0,len(val2)):
    n1=n2=n3=0
    n2=ord(val1[i])
    n3=ord(val2[i])
    n1=n2+n3
    if n1>96 and n1<123:
        print(chr(n1),end="")
    elif (n1-96)<122 and(n1-96)>96:
        n1=n1-96
        print(chr(n1),end="")
    elif n1>148:
        n1=n1-96-26
        print(chr(n1), end="")
    else:
        n1=n1-26
        print(chr(n1), end="")
