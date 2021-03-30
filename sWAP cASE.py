def swap_case(s):
	L=[]
	for i in range (0,len(s)):
		if s[i] == s[i].lower():
			L.append(s[i].upper())
		elif s[i] == s[i].upper():
			L.append(s[i].lower())
		else:
			L.append(s[i])
	return "".join(L)