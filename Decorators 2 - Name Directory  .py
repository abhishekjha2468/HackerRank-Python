n,list=int(input()),[]
for _ in range(n): list.append(input().split())
list.sort(key=lambda x: int(x[-2]))
for i in list:
	if i[-1]=="M": print("Mr. "+" ".join(i[:-2]))
	else: print("Ms. "+" ".join(i[:-2]))