numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# max=numbers[0]
# maxa=numbers[0]
# while i< len(numbers):
#     if numbers[i]>max:
#         max=numbers[i]
#     elif numbers[i]>maxa and numbers[i]<max:
#             maxa=numbers[i]
#     i+=1
# print(max)
# print(maxa)          



i=0
min=numbers[0]
mina=numbers[0]
while i< len(numbers):
    if numbers[i]<min:
        min=numbers[i]
    elif numbers[i]<mina and numbers[i]>min:
            mina=numbers[i]
    i+=1
print(min)
print(mina)          
