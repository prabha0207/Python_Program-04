import math
f,g=input().split()
e=math.gcd(int(f),int(g))
print((int(f)*int(g))//e)
