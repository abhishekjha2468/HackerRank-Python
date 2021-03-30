def minion_game(string):
	a=string
	p1=[]
	p2=[]
	for i in range(1,len(a)+1):
		if a[i-1] in list('AEIOU'): p2.append((len(a)-i)+1)
		else: p1.append((len(a)-i)+1)
	if sum(p1)>sum(p2): print(f'Stuart {sum(p1)}')
	elif sum(p2)>sum(p1): print(f'Kevin {sum(p2)}')
	else: print(f'Draw')