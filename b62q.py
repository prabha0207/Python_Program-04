value=input()
a=0
for i in value:
    if(0<=int(i)<=1):
        a+=1
if(int(len(value))==a):
    print("yes")
else:
    print("no")
