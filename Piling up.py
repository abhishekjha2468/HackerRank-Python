for _ in range(int(input())):
	n=int(input())
	list=[*map(int, input().split())]
	sample=(sorted(list))[::-1]
	new_list=[]
	for i in range(n):
		max_num = max(list[0],list[-1])
		new_list.append(max_num)
		list.remove(max_num)
	if sample == new_list: print("Yes")
	else: print("No")			