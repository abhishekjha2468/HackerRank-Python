for _ in range(int(input())):
	n,list=int(input()),[*map(int, input().split())]
	min_num=min(list)
	index=list.index(min_num)
	l1=sorted(list[:index])[::-1]
	l2=sorted(list[index:])
#	print("l1: ",l1)
#	print("l2: ",l2)
	new_list=l1+l2
#	print("new_list: ",new_list)
	print("Yes" if new_list== list else "No")