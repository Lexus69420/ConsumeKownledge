import math
import time
t=time.time()
def prem(k):
    
    for i in range(2,math.ceil(k**0.5)+1):
        if k  % i == 0:
           return False 

    return True

s=0
x=3



stop=2000000
while not (x>stop):
    if prem(x)==True:
        s+=x
        
       
        x+=2
        
    else:
        x+=2
         
k=time.time()-t
print(k)
print(s+2)

