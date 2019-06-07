num1,num2=map(int,input().split(" "))
num3,num4=map(int,input().split(" "))
num5,num6=map(int,input().split(" "))
if(num1==num3==num5):
    print("yes")
elif(num2==num4==num6):
    print("yes")
elif(num1==num2 and num3==num4 and num5==num6):
    print("yes")
else:
    print("no")
