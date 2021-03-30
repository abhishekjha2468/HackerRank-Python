import numpy
n,m,p=(map(int, input().split()))
list=[]
for _ in range(n+m): list.append([*map(int, input().split())])
print(numpy.array(list))