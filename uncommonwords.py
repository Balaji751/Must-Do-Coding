
def uncommon(s1,s2):
	sr1=s1.split(" ")
	sr2=s2.split(" ")
	uncommon=""
	for i in sr1:
		if i not in sr2:
			uncommon=uncommon+" "+i
	return uncommon

s1=input("Enter string1:")
s2=input("Enter string2:")
result=uncommon(s1,s2)
print(result)