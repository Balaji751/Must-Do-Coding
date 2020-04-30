
def great(str,x):
	s=str.split(" ")
	for word in s:
		if len(word)>x:
			print(word)
	else:
		print("No words greater than given length")

str=input()
x=int(input("Enter the length of word:"))
result=great(str,x)

