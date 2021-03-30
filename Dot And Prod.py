import numpy
numpy.set_printoptions(legacy = '1.13')
n=int(input())
a,b=[],[]
for _ in range(n): a.append([*map(int, input().split())])
for _ in range(n): b.append([*map(int, input().split())])
A=numpy.array(a)
B=numpy.array(b)
print(numpy.dot(A, B))