x=[*map(int, input().split())]
n,m=x[0],x[1]
list=[]
for i in range(n):
	list.append([*map(int, input().split())])
#print("list: ",list)
zipped_list=[*zip(*list)]
#print("zipped_list: ",zipped_list)
k=int(input())
#print("k: ", k)
list_sort=sorted([*map(int, set(zipped_list[k]))])
#print("list_sort: ", list_sort)
for i in list_sort:
	for j in list:
		if i == j[k]:
			print(*map(lambda x: f'{x}',j))
			break