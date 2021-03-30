a=int(input())
L=[str(i.strip()) for i in input().split()]
index=L.index('MARKS')
m=[]
for j in range(0,a):
	l=[str(k.strip()) for k in input().split()]
	m.append(int(l[index]))
print("{0:.2f}".format((sum(m)/a)))