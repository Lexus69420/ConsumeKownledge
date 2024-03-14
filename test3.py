max=0
k=[3,4,23,4,9,27]
for i in range(1,len(k)-1):
    if k[i+1]>k[i]:
        max=k[i+1]
    else:
        max=k[i]
print(max)        

