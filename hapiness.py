n=input("")
C=[int(i) for i in input("").split()]
A=[int(i) for i in input("").split()]
B=[int(i) for i in input("").split()]
hapiness=0
for i in range (0, len(C)):
	if C[i] in A:
		hapiness=hapiness+1
	elif C[i] in B:
		hapiness=hapiness-1
print(hapiness)