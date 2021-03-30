import numpy
dimensions=[*map(int, input().split())]
n=dimensions[0]
m=dimensions[1]
list=[]
for i in range(n): list.append([ *map( int , input().split())])
my_array = numpy.array(list)
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array, axis = None),12))