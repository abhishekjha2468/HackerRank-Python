def solve(s):
	L=s.split()
	l=[]
	for i in range (0,len(L)):
		l.append(str((L[i]).capitalize()))
		s=s.replace(L[i],l[i])
	return s