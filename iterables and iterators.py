from math import factorial as fac
from itertools import combinations as com
a,list,k=int(input()), input().split(), int(input())
count=0
index_of_a=[]
for n in range(len(list)):
	if list[n]=='a': index_of_a.append(n+1)
for i in com([*range(1,a+1)],k):
	for j in index_of_a:
		if j in i:
			count=count+1
			break
		else: pass
p=count/((fac(a))/(fac(a-k)*fac(k)))
print(p)