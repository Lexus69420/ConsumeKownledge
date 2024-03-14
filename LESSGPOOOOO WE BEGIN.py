i=1
j=2
k=i+j
f=0
s=0
while (k<4000000):
    f=k+ j
    j=k
    k=f
    if f%2==0:
        s=s+f
print(s)  
    
