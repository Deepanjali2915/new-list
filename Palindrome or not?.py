# word=input("Enter the word: ")
# i=0
# a=[]
# while i<len(word):
#     a.append(word[-i])
#     i+=1
# if a==word:
#     print("Palindrome")
# else:
#     print("not palindrome")
        

word=input("Enter the name: ")
a=len(word)-1
b=[]
while a+1:
    b.append(word[a])
    a-=1
if list(b)==list(word):
    print("palindrome")
else:
    print("not")                

