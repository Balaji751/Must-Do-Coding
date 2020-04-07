a=54321
rev=0
while(a>0):
    b=a%10
    rev=rev*10+b
    a=int(a/10)
print(rev)