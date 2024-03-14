

k=20
list=[]
list2 = [0]*k


for i in range(k):
    k2=k-i
    
    list.append(k2)

var=k+1
for i in range(k) :
    var+=list[i]
      
print(list)



def path():
    global list,list2
    som=0
    for i in range(k):
        som+=list[i]

    print(som)
    
    list2[0]=som
    
    for i in range(1,k):
        
        list2[i]=list2[i-1]-list[i-1]


    for i in range(k):
        list[i]=list2[i]

    
    last=0
    for i in range(k):
        last+=list[i]
              
    return last

sum=0
for i in range(k-3):
    sum+=path()
print((sum+var)*2)






    




