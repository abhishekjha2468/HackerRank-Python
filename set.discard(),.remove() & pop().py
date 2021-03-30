a=int(input())
l=[int(i) for i in input().split()]
s=set(l)
b=int(input())
for i in range (0,b):
	c=[str(j) for j in input().split()]
	if c[0]=='pop':
		s.pop()
	elif c[0]=='remove':
		s.remove(int(c[1]))
	elif c[0]=='discard':
		s.discard(int(c[1]))
print(sum(s))