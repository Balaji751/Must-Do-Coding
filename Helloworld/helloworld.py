n=int(input("Enter a number: "))
fact=1
while n>0:
	fact=fact*n
	n-=1
print(f'Factorial of a number is : {fact}')