import itertools
L=[int(i) for i in input().split()]
S=[]
x=[]
for j in range(0,L[0]):
	a=[int(i)*int(i) for i in input().split()]
	x.append(int((a[0])**(0.5)))
	a.pop(0)
	S.append(a)
A = list(itertools.product(*S))
l=A
B=[]
for i in l:
	B.append((sum(i))%L[1])
print(max(B))
