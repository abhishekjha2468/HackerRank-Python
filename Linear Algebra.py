import numpy
n=int(input())
list=[]
for i in range(n):
	list.append([ float(i) for i in input().split()])
print(round(numpy.linalg.det(list),2))