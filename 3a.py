sentance=input("enter a sentance")
wordlist=sentance.split(" ")
print("the sentance has: ",len(wordlist),"words")
digcnt=upcnt=locnt=0

for ch in sentance:
    if ch.isdigit():
        digcnt +=1
    elif ch.isupper():
        upcnt +=1
    elif ch.islower():
        locnt +=1

print("the sentance has: ",digcnt,"digits\n",upcnt,"uppercase letter\n",locnt,"lowercase letter\n")
