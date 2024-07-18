import random

def msort(list):
    if len(list)>1:
        mid=len(list)//2
        lefthalf=list[:mid]
        righthalf=list[mid:]
        msort(lefthalf)
        msort(righthalf)
        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                list[k]=lefthalf[i]
                i+=1
            else:
                list[k]=righthalf[j]
                j+=1
            k+=1
        while i<len(lefthalf):
            list[k]=lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            list[k]=righthalf[j]
            j+=1
            k+=1
    return list

def insort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        
list=[]
for i in range(10):
    list.append(random.randint(0,999))
print("\n Unsorted list")
print(list)
print("Sorting using insertion sort")
insort(list)
print(list)

list=[]
for i in range(10):
    list.append(random.randint(0,999))
print("\n Unsorted list")
print(list)
print("Sorting using merge sort")
msort(list)
print(list)
            
