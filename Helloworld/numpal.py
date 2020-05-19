n=int(input())
temp=n
t=0
while n>0:
	c=n%10
	# print(c)
	t=t*10+c
	print(t)
	n=n//10
	# print(n)
if temp==t:
	print("True")
else:
	print("False")