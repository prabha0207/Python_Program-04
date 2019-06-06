a1=int(input())
if a1 > 1:  
   for x in range(2, a1//2): 
       if (a1 % x) == 0: 
           print("yes") 
           break
   else: 
       print("no") 
  
else: 
   print("yes")
