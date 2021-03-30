import numpy
num=[int(i) for i in input().split()]
list=[]
for i in range (0,num[0]):
	l="[" + input("") + "]"
	list.append(l)
for i in range (0,num[1]):
	l="[" + input("") + "]"
	list.append(l)
c=1
for i in list:
	if c==1:
		print(f'[{i}')
		pass
	if c==len(list):
		print(f'{i}]')
		break
	print(i)
	c=c+1