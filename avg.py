m=int(input(""))
list=[]
for i in range(0,m):
	a=input("")
	list.append(a)
name=input("")
sum=0.00
for j in range(0,m):
	if name in list[j]:
		b=str(list[j])
		c=b.split()
		c.pop(0)
		for i in range(0,len(c)):
			sum=sum+float(c[i])
		avg=sum/(len(c))
		print('%.2f'%avg)