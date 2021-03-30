a=[ int(i) for i in input().split() ]
L=[]
for j in range(a[1]):
	L.append([ float(i) for i in input().split() ])
for i in zip(*L):
	print(sum(i)/a[1])