def solve(s):
	L=s.split()
	l=""
	for i in range (0,len(L)):
		if i!=len(L)-1:
			l=l+L[i][0].upper()+L[i][1::].lower() +" "
		else:
			l=l+L[i][0].upper()+L[i][1::].lower()
	return l