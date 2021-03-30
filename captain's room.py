n=int(input())
list=[ int(i) for i in input().split()]
for i in list:
	if list.count(i)<n:
		print(i)