integers=[int(i) for i in input().split()]
n=integers[0]
m=integers[1]
list=[int(i) for i in input().split()]
A={int(i) for i in input().split()}
B={int(i) for i in input().split()}
happiness=0
for i in range(n):
	if list[i] in A:
		happiness=happiness+1
	if list[i] in B:
		happiness=happiness-1
print(happiness)