a=[*map(int, input().split())]
n,m=a[0],a[1]
L=[]
for i in range(n): L.append(min([*map(int, input().split())]))
print(max(L))