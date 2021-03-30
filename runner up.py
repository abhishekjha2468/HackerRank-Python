k=input("")
num=[int(i) for i in input().split()]
max1=max(num)
while max1 in num:
	index=num.index(max1)
	num.pop(index)
print(max(num))