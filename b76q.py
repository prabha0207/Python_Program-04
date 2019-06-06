f=int(input())
if num1 > 1:  
   for i in range(2, f//2): 
       if (f % i) == 0: 
           print("yes") 
           break
   else: 
       print("no") 
  
else: 
   print("yes")
