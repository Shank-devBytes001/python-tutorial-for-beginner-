a=input("enter a value")
if a==a[::-1]:
    print("it is a palindrome ")
else:
    print("the given is not a palindrome ")

for i in range(len(a)):
    if a.count(a[i])>0:
               print(a[i],"appears",a.count(a[i]),"times")
    
