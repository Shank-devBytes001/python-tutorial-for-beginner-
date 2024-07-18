import re

def isph(num):
    if len(num)!=12:
        return False
    for i in range(len(num)):
        if i==3 or i==7:
            if num[i]!="-":
                return False
            else:
                if num[i].isdigit==False:
                    return False

    return True


def chkp(num):
    pat=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pat.match(num):
        return True
    else:
        return False

phno=input("enter the phone number: ")
print("without using the regular expression")
if isph(phno):
    print("valid phno")
else:
    print("invalid phno")

print("using the regular exp")
if chkp(phno):
    print("valid phno")
else:
    print("invalid phno")
