def divisors(k):
    div=2
    occ=[]
    kawasm=[]
    while (div<=k):
        if k%div==0:
            if div not in occ:
                occ.append(div)
            kawasm.append(div)    
            k=k//div
        else:
            div+=1
    i=0
    s=0
    final=[]
    while(i<len(occ)):
        for j in range(len(kawasm)):
            if occ[i]==kawasm[j]:
                s=s+1
        final.append(s)
        s=0
        i+=1
    

    numdivis=1
    for i in range(len(final)):
        numdivis=numdivis*(final[i]+1)
    
    return numdivis
        

            





f=1
divis=1
x=2
while (divis<=500):
    
    f=f+x
    divis=divisors(f)
    print(divis)
    if divis>=500:
        print(f)
    else:
        x+=1
        divis=1
   
        
    


           

    