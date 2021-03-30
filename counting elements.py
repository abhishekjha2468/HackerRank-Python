string=input()
count=1
list=[]
for i in range(len(string)):
	try:
		if i<(len(string)-1):
			if string[i]==string[i+1]:
				count=count+1
			else:
				list.append((count,int(string[i])))
				count=1
		else:
			list.append(count,int(string[i]))
	except:
		list.append((count,int(string[i])))
for i in list:
	print(i,end=" ")