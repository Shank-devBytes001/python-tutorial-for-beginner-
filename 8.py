class palstr:
    def __init__(self):
        self.ispali=False

    def ckhp(self,st):
        if st==st[::-1]:
            self.ispali=True
        else:
            self.ispali=False

        return self.ispali

class palint(palstr):
    def __init__(self):
        self.ispali=False

    def ckhp(self,val):
        temp=val
        rev=0
        while temp!=0:
            dig=temp%10
            rev=(rev*10)+dig
            temp=temp//10

        if val == rev:
            self.ispali = True
        else:
            self.ispali=False
        return self.ispali

str=input("enter the string value: ")
strobj=palstr()
if strobj.ckhp(str):
    print("it is a palindrome")
else:
    print("not a palinsrome")

val=int(input("enter the value in number : "))
intobj=palint()
if intobj.ckhp(val):
    print("it is a palindrome")
else:
    print("not a palinsrome")
