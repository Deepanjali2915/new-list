elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
counta=0
even=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        count+=1
    else:
        counta+=1
    i+=1    
print("Even",count)
print("Odd",counta)        