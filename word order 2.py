a=int(input())
list=[]
for j in range(0,a):
	list.append(input())
b=set(list)
print(len(b))
for i in range(0,len(b)):
	print(list.count(list[0]),end=" ")
	list.remove(list[0])