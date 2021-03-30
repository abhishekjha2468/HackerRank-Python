import numpy
numpy.set_printoptions(legacy = '1.13')
num=tuple(map(int, input().split()))
print(numpy.zeros(num, dtype=numpy.int),numpy.ones(num, dtype=numpy.int),sep='\n')