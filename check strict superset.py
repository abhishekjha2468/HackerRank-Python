u=[int(i) for i in input().split()]
U=set(u)
n=int(input())
x=[]
for i in range(0,n):
	a=[int(i) for i in input().split()]
	A=set(a)
	if set(a+u)==set(u) and A!=U:
		x.append(True)
	else:
		x.append(False)
if len(set(x))==1:
	print(x[0])
else:
	print(False)