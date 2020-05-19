a=[12,11,9,3,2,1]
for i in range(len(a)):
	for j in range(0,len(a)-i-1):
		if a[j]>a[j+1]:
			a[j],a[j+1]=a[j+1],a[j]
for i in range(len(a)):
	print(a[i])



for i in range(int(input()):
	n=int(input())
	a=list(map(int,input().split()))
	p=1

	for i in range(n):
		p=p*a[i]

	for i in range(n):
		print(p//a[i],end=" ")