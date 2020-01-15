#Input a number from user and print in word(Ex: 1234=>OneTwoThreeFour)

while True:
	str=input("Enter a number: ")
	for i in str:
		if(ord(i)>57 or ord(i)<48):
			print("Enter only an Integer")
		else:
			break
	break
print()
print("Number",str,"in words:\n")
tup=('Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine')
for i in str:
	k=ord(i)-48
	print(tup[k],end="")


