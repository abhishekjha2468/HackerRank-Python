a=int(input())
list=[]
v=[]
for i in range(0,a):
	s=[str(j) for j in input().split()]
	x=" ".join(s[:(len(s)-1):])
	y=int(s[len(s)-1])
	if x not in list:
		list.append(x)
		v.append(y)
	elif x in list:
		index=list.index(x)
		v[index]=v[index]+y
for i in range(0,len(list)):
	print(list[i],v[i])