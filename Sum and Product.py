dimension=input().split()
n=int(dimension[0])
m=int(dimension[1])
list=[]
for i in range(n): list.append(map(int, input().split()))
new_list=zip(*list)
s=[]
product=1
for i in new_list: s.append(sum(i))
for i in s: product=product*i
print(product)