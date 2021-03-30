import numpy
list,(n,m)=[],(map(int, input().split()))
for _ in range(n): list.append([*map(int, input().split())])
print(numpy.transpose(numpy.array(list)),(numpy.array(list)).flatten(),sep="\n")