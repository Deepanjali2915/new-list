elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
suma=0
count=0
counta=0
while i<len(elements):
    if elements[i]%2==0:
        count+=1
        sum=sum+elements[i]
    else:
        counta+=1
        suma=suma+elements[i]
    i+=1
print("Even",sum/count,count)
print("Odd",suma/counta,counta)            
