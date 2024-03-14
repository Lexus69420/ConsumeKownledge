import math

stop=False
def test(s):
    if s/s==1:
        return True
    else:
        return False




for a in range(1,1000):
    for b in range(2,1000):
        c=(a**2)+(b**2)
        
        if test(c)==True:
            mraba3=math.sqrt(c)
            if (a+b+mraba3)==1000:
                print(a*b*mraba3)
      
print('done')
       