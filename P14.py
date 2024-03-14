def collatz(n,lista,lista2):
    cmpt=0
   
    while (n!=1):
        if n%2==0:
            n=n/2
            cmpt+=1
        else:
            n=n*3+1
            cmpt+=1
    return cmpt
    
    

list=[]
list2=[]
for i in range(1,1000000):
    k=collatz(i,list,list2)
max=list[0]
for i in range(1,len(list)):
    if max<list[i] :
        max=list[i]
        print(list2[i])
print(collatz(13,list,list2))
print(list)
print(list2)   
