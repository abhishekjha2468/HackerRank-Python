n=int(input(""))
A=[]
for i in range (0,n):
	list=input("").split()
	a=list[0]
	if a=='insert':
		A.insert(int(list[1]),int(list[2]))
	elif a=='print':
		print(A)
	elif a=='remove':
		A.pop(A.index(int(list[1])))
	elif a=='append':
		A.append(int(list[1]))
	elif a=='sort':
		A.sort()
	elif a=='pop':
		A.pop()
	elif a=='reverse':
		A.reverse()