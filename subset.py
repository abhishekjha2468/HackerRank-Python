n=int(input())
for i in range(0,n):
	a=int(input())
	A=[int(j) for j in input().split()]
	b=int(input())
	B=[int(j) for j in input().split()]
	C=set(A+B)
	if len(C)==len(set(B)):
		print(True)
	else:
		print(False)