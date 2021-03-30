from itertools import product
n=[int(i) for i in input().split()]
m=[int(i) for i in input().split()]
A=[n,m]
L=list(product(*A))
string=""
for i in L:
	string=string+str(i)+" "
print(string)