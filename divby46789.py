lis1=[]
lis2=[]
lis3=[]
lis4=[]
for i in range(1,101):
	if i%2==0:
		lis1.append(i)
	else:
		lis2.append(i)
for i in lis1:
	if i%4 or 6 or 8 or 10 or 3 or 5 or 7 or 9 ==0:
		lis3.append(i)
for i in lis2:
	if i%4 or 6 or 8 or 10 or 3 or 5 or 7 or 9 ==0:
		lis4.append(i)
print(lis3)
print(lis4)