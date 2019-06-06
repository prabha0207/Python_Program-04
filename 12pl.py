x,b = map(int,input().split())
b = b%x
l1 = list(map(int,input().split()))
l2 = l1[-b:] + l1[:-b]
print(*l2)
