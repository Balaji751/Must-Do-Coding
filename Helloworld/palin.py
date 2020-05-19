a=int(input())
temp=a
t=0
while(a>0):
	c=a%10
	t=t*10+c
	a=a//10
if temp==t:
	print("Yes")
else:
	print("No")