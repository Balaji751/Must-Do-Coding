a=int(input())
b=(bin(a)[2:])
c=str(b)
d=len(c)
e=32-d
f=str("0"*e)+c
count=0
for i in f:
    if i=="1":
        count+=1
print(count)