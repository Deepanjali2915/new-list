elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0;sum=0;count=0;average=0
odd=0;suma=0;counta=0;averagea=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        count+=1
        average=sum/counta
    else:
        suma=suma+elements[i]
        counta+=1
        averagea=suma/counta
    i+=1    
print("Even\n",sum,"\n",count,"\n",average)
print("Odd\n",suma,"\n",counta,"\n",averagea)
