m1=int(input("enter the marks of test1= "));
m2=int(input("enter the marks of test2= "));
m3=int(input("enter the marks of test3= "));

if m1<=m2 and m1<=m3:
    avgm=(m2+m3)/2
elif m2<=m1 and m2<=m3:
    avgm=(m1+m3)/2
elif m3<=m1 and m3<=m2:
    avgm=(m1+m2)/2

print("the best of the 2 tests is= ",avgm)











