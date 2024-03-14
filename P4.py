def palin(num):
    reverse=""
    for i in range (len(num)):
       reverse=num[i]+reverse
    if reverse==num:
      return True
       
    else:
      return False


palind=0
for i in range (100,999):
    for j in range(100,999):
      num=i*j
      if palin(str(num))==True:
         while (palind < num ):
           palind=num
     
print(palind)