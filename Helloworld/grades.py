a=list(map(int,input().split(" ")))
print(sum(a))
lis=[]
for i in a:
	if i!=a[1]:
		if i>=91 and i<=100:
			print("A1 10")
			lis.append(10)
		elif i>=81 and i<=90:
			print("A2 9")
			lis.append(9)
		elif i>=71 and i<=80:
			print("B1 8")
			lis.append(8)
		elif i>=61 and i<=70:
			print("B2 7")
			lis.append(7)
		elif i>=51 and i<=60:
			print("C1 6")
			lis.append(6)
		elif i>=41 and i<=50:
			print("C2 5")
			lis.append(5)
		elif i>=35 and i<=40:
			print("D1 4")
			lis.append(4)
		else:
			print("D2 3")
			lis.append(3)
	else:
# print("Second language grade")
		if i>=90 and i<=100:
			print("A1 10")
			lis.append(10)
		elif i>=79 and i<=89:
			print("A2 9")
			lis.append(9)
		elif i>=68 and i<=78:
			print("B1 8")
			lis.append(8)
		elif i>=57 and i<=67:
			print("B2 7")
			lis.append(7)
		elif i>=46 and i<=56:
			print("C1 6")
			lis.append(6)
		elif i>=35 and i<=45:
			print("C2 5")
			lis.append(5)
		elif i>=20 and bi<=34:
			print("D1 4")
			lis.append(4)
		else:
			print("-")
sum=0
res=0
for i in lis:
	sum+=i
res=sum/6
print(res)
