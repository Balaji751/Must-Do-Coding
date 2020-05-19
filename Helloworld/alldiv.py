a=input()
b=list(a)
lis=[]
for i in b:
	try:
		if int(a)%int(i)==0:
			lis.append(1)
		else:
			lis.append(0)
	except ZeroDivisionError:
		break
# print(lis)

if 0 in lis:
	print("No")
else:
	print("Yes")