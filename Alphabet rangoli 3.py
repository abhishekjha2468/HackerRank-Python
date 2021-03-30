def print_rangoli(n):
	string="abcdefghijklmnopqrstuvwxyz"
	Lest=list(string)
	k=n
	c=2
	L=[]
	for i in range(k-1,-1,-1):
		star=(2*n)-c
		List=[]
		if i==(k-1):
			List.append(Lest[k-1])
		for j in range (n-1,i,-1):
			List.append(Lest[j])
			List.append("-")
		f="-"*star
		if i!=k-1:
			l=f+"".join(List)+string[i]+"".join(List[::-1])+f
		else:
			l=f+"".join(List)+f
		print(l)
		L.append(l)
		c=c+2
	for i in range(len(L)-2,-1,-1):
		print(L[i])
