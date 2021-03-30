from collections import counter
n=int(input())
list=input().split()
x, y = Counter(list).most_common()[-1]
print(x)
for i in list:
	if list.count(i)<n:
		print(i)