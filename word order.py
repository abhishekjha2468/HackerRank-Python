a=int(input())
L=[]
for i in range(a): L.append(input())
print(len(set(L)))
i=0
while(L!=[]):
	print(L.count(L[i]),end=" ")
	L= list(filter(lambda a: a != L[i], L))