l=[*map(int, input().split())]
n,m=l[0],l[1]
list=[]
for i in range(n): list.append([*map(int, input().split())])
k=int(input())
list.sort(key=lambda x: x[k] )
for i in list:
	print(*i,sep=' ')