x=int(input())
y=int(input())

def ppcm(x,y):

    if x>y:
        sup=x
        inf=y
    else:
        inf=x 
        sup=y

    i=1
    while not((sup*i) % inf == 0):
      i=i+1
    return(sup*i)  


  
  
sum=ppcm(x,y)
print(sum)
