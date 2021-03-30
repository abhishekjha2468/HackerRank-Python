a=int(input())
list=[]
l=[]
c=[]
for j in range(0,a):
	list.append(input())
	if list[j] not in l:
		l.append(list[j])
		c.append('1')
	elif list[j] in l:
		index=l.index(list[j])
		c[index]=str(int(c[index])+1)
print(len(set(list)))
print(" ".join(c))