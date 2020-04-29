s1=str(input("Enter the String:"))
s1=s1.split(" ")
for word in s1:
	if len(word)%2==0:
		print(word)