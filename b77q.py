val1=int(input())
val2=''
if(val1>1):
    for i in range(1,val1+1):
        val3=val1%i
        if(val3==0):
            val2=val2+str(i)+" "
print(val2)
