a=int(input())
A=[int(i) for i in input().split()]
b=int(input())
B=[int(j) for j in input().split()]
m=list((set(A)-set(B)))+list((set(B)-set(A)))
for i in range(0,len(m)):
	print(min(m))
	m.pop(m.index(min(m)))