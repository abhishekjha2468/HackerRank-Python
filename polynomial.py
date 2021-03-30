import numpy

L=[float(i) for i in input("").split()]

a=int(input(""))

print(numpy.polyval(L,a))