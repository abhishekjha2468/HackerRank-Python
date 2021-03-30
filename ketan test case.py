l = input().split()
m, k = int(l[0]), int(l[1])
b = []
for i in range(0,m):
    a = [map(int, input().split())]
    b.append(max(a)**2)
c = sum(b)
print(c%k)()