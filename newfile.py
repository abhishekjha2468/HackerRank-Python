def count_substring(s,ele):
	a=int(len(s))
	b=int(len(ele))
	c=0
	for i in range (0,a-b+1):
		if s[i:i+b]==ele:
			c=c+1
	return c
	
