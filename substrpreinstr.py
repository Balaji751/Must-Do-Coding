def present(s1,s2):
	if(s2 in s1):
		print("Yes")
	else:
		print("No")

s1=str(input("Enter the string:"))
s2=str(input("Enter the substring:"))
present(s1,s2)