n=int(input(""))
name=[]
score=[]
for i in range (0,n):
	name.append(input(""))
	score.append(float(input("")))
S=min(score)
C=score.count(S)
for i in range(0,C):
	index=score.index(S)
	name.pop(index)
	score.pop(index)
m=min(score)
count=score.count(m)
list=[]
for i in range (0,count):
	index=score.index(m)
	list.append(name[index])
	name.pop(index)
	score.pop(index)
list.sort()
for i in list:
	print(i)