import numpy
numpy.set_printoptions(legacy = '1.13')
my_array=numpy.array([*map(float, input().split())])
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))