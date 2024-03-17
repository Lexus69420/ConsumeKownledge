def count(ch):
    sum=0
    for i in range (len(ch)):
        sum+=1
    return sum
all=[]
twentyto100=[]
sizes=["one","two","three","four","five","six","seven","eight","nine","ten","Eleven", "Twelve" , "Thirteen","Fourteen","Fifteen","Sixteen", "Seventeen","Eighteen","Nineteen" ]
sizes2=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundreds=[]
hundreds2=[]
hundreds3=[]
hundreds4=[]
hundreds5=[]

for i in range(8):
    for j in range(9):
        twentyto100.append(sizes2[i]+sizes[j])
        

for i in range(9):
    hundreds.append(sizes[i]+"hundred")
    

for i in range(9):
    for j in range(len(sizes)):
        hundreds2.append(hundreds[i]+"and"+sizes[j])

for i in range(9):
    for j in range(len(sizes2)):
        hundreds3.append(hundreds[i]+"and"+sizes2[j])

for i in range(8,9):
    for j in range (len(twentyto100)):
        hundreds5.append(hundreds[i]+"and"+twentyto100[j])


for i in range(8):
    for j in range (len(twentyto100)):
        hundreds4.append(hundreds[i]+"and"+twentyto100[j])


all=all+twentyto100+sizes+sizes2+hundreds+hundreds2+hundreds3+hundreds4+hundreds5
print(all)
