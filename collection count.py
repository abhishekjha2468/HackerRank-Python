a=int(input())
L=[int(i) for i in input().split()]
n=int(input())
s=[]
for i in range(0,n):
	l=[int(i) for i in input().split()]
	if l[0] in L:
		s.append(l[1])
		L.pop(L.index(l[0]))
print(sum(s))
	