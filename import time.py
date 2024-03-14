import math
def prem(x):
    test=True
    for i in range(2,math.ceil(x**0.5)):
        if x % i == 0:
           test==False 
        
    if test==True :
            return True
    else:
            return False
           

    

print(prem(14))