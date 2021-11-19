# a=[]
# s=0
# b=0
# size=int(input("Enter the size: "))  




# a=[1,1,1,1,1,0,1,1]
# i=0
# sum=0
# sum1=0
# number=6
# while i<len(a):
#     b=a[number]
#     sum=(2**i*b)
#     number-=1
#     i+=1
#     sum1+=sum
# print(sum1)        




num = int(input("Enter the Binary Number: "))
i= 0
m = 1
length = len(str(num))
for k in range(length):
    reminder = num % 10
    i=i+ (reminder * m)
    m = m * 2
    num = int(num/10)

print("Equivalent Decimal Value = ",i)