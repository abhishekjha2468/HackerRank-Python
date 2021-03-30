from collections import deque
d = deque()
a=int(input())
for i in range(0,a):
	c=[str(j) for j in input().split()]
	if c[0]=='append':
		d.append(int(c[1]))
	elif c[0]=='appendleft':
		d.appendleft(int(c[1]))
	elif c[0]=='clear':
		d.clear()
	elif c[0]=='extend':
		d.extend(int(c[1]))
	elif c[0]=='extendleft':
		d.extendleft(int(c[1]))
	elif c[0]=='count':
		d.count(int(c[1]))
	elif c[0]=='pop':
		d.pop()
	elif c[0]=='popleft':
		d.popleft()
	elif c[0]=='extend':
		d.extend(int(c[1]))
	elif c[0]=='remove':
		d.remove(int(c[1]))
	elif c[0]=='reverse':
		d.reverse()
	elif c[0]=='rotate':
		d.rotate(int(c[1]))
c=" ".join([str(i) for i in d])
print(c)