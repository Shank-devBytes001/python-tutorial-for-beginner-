roman=input("enter the roman letters: ")
r_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
result =0

for i in range(len(roman)):
    if i>0 and r_dict[roman[i]]>r_dict[roman[i-1]]:
        result += r_dict[roman[i]]-2*r_dict[roman[i-1]]
    else:
        result += r_dict[roman[i]]

print("the decimal equivalance of ",roman," is ",result)
        
