k= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
a=0
b=0
c=0
while i<len(k):
    if k[i]>=10000000:
        a+=1
        # print("crorpati",a)
    elif k[i]<10000000 and k[i]>100000:
        b+=1
        # print("Lakhpati",b)
    else:
        c+=1
        # print("Diwaliya",c)
    i+=1        
print("crorpati",a)
print("Lakhpati",b)
print("Diwaliya",c)

