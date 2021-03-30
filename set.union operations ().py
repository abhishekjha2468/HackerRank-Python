a=int(input())
A=[int(i) for i in input().split()]
b=int(input())
B=[int(i) for i in input().split()]
C=A+B
print(len(set(C)))