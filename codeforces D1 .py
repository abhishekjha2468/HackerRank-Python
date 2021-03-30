from itertools import permutations
def Max(perm, n):
	a=[]
	b=[]
	for i in perm:
#		print(i)
#		l=list(i)
		c=0
		for j in range(1,n-1):
			if(i[j-1]>i[j]) and (i[j+1]>i[j]):
				c=c+1
		a.append(i)
		b.append(c)
	index=b.index(max(b))
	print(b[index])
	for k in a[index]:
		print(f'{k} ',end="")



n=int(input(""))
s=input("")
S=s.split(" ")
L=[]
for i in S:
	L.append(int(i))
perm= permutations(L)
Max(perm, n)
