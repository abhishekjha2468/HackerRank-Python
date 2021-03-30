L=[int(i) for i in input().split()]
A=[]
B=[]
for i in range(0,L[0]):
	A.append(input())
for i in range(0,L[1]):
	B.append(input())
for j in range(0,len(B)):
	for k in range(0,len(A)):
		if B[j]==A[k]:
			print(k+1,end=" ")
	if B[j] not in A:
		print(-1,end=" ")
	print()