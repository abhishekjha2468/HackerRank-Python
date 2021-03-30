import numpy
numpy.set_printoptions(legacy = '1.13')
n,m=(map(int, input().split()))
A,B=[],[]
for _ in range(n): A.append([*(map(float, input().split()))])
for _ in range(n): B.append([*(map(float, input().split()))])
a = numpy.array(A , int)
b = numpy.array(B , int)
print(a+b,a-b,a*b,a//b,a%b,a**b,sep="\n")