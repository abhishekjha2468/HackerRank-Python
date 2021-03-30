a=int(input())
A=[int(i) for i in input().split()]
b=int(input())
B=[int(i) for i in input().split()]
C=set(A).intersection(set(B))
print(len(set(C)))