str1=input("enter the 1st string: ")
str2=input("enter the 2nd string: ")

if len(str1)<len(str2):
    short=len(str1)
    long=len(str2)

else:
    short=len(str2)
    long=len(str1)

matchcnt=0

for i in range(short):
    if str1[i]==str2[i]:
        matchcnt +=1

print("the similarities between both is: ")
print(matchcnt/long)
        
