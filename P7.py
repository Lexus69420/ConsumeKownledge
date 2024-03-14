import time
import math
k=(time.time())
print(k)
time.sleep(2)
prime=0
t=7
def isprime(n):
    test=True
    for i in range(2,math.ceil(n**0.5)):
        if n % i ==0:
            test = False
            
    if test==True :
        return True
    else:
        return False




print(isprime(14))



