import sys, string, math
def isPalin(x) :
    if len(x) == 1 : return False
    if x == x[::-1] : return True
    return False

x = input()
n = len(x)
for i in range(n-1,0,-1) :
    for j in range(0,n-i) :
        i1 = j
        i2 = j+i+1
        s2 = s[i1:i2]
        #print(i1,i2-1,s2)
        if isPalin(s2) :
            #print(s2)
            print(n-len(s2))
            sys.exit()
