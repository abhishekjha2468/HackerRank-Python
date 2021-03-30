from itertools import combinations_with_replacement
line=input("")
l=line.split()
word=list(str(l[0]))
count=int(l[1])
f=[]
for i in range(0,1):
	list=[]
	comb=combinations_with_replacement(word,count)
	for i in comb:
		list.append("".join(i))
	list.sort()
	w=[]
	for i in list:
		k=[]
		for j in range (0,len(i)):
			k.append(i[j])
		k.sort()
		w.append("".join(k))
	w.sort()
	f=f+w

for i in f:
	print(i)