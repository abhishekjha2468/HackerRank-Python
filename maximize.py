L=[int(i) for i in input().split()]
S=[]
for i in range (0,L[0]):
	l=[int(j) for j in input().split()]
	list=[]
	for k in range(0,len(l)):
		list.append(l[k]**2)
	S.append((max(list)))
print(sum(S)%L[1])