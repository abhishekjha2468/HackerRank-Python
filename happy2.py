n=input("")
C=input("").split()
A=input("").split()
B=input("").split()
hapiness=0
for i in C:
	if i not in A and i not in B:
		pass
	if i in A:
		hapiness=hapiness+1
	elif i in B:
		hapiness=hapiness-1
print(hapiness)