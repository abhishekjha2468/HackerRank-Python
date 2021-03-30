from itertools import permutations
line=input("")
l=line.split()
word=list(str(l[0]))
count=int(l[1])
comb=permutations(word,count)
list=[]
for i in comb:
	list.append("".join(i))
list.sort()
for i in list:
	print(i)