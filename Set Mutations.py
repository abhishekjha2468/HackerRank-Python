a=int(input())
m=[int(i) for i in input().split()]
l=set(m)
b=int(input())
for i in range (0,b):
	x=[str(j) for j in input().split()]
	y=[int(k) for k in input().split()]
	s=set(y)
	c=x[0]
	if c=='intersection_update':
		l.intersection_update(s)
	elif c=='update':
		l.update(s)
	elif c=='symmetric_difference_update':
		l.symmetric_difference_update(s)
	elif c=='difference_update':
		l.difference_update(s)
print(sum(l))