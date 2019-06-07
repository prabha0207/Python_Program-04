val1=input()
val2=len(val1)
val3=[]
for i in val1:
    val3.append(i)
if(val2%2==0):
    val3[val2//2]="*"
    val3[(val2//2)-1]="*"
else:
    val3[val2//2]="*"
val1=''
for i in val3:
    val1=val1+i
print(val1)
