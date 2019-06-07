s=input()
substring=""
l=0
op=[]
if s==s[::-1]:
  op.append(0)
for y in range(len(s)-1):
  for z in range(y+1,len(s)):
    substring=s[y:z+1]
    if substring==substring[::-1]:
      op.append(len(s)-len(substring))
     
print(min(op))
