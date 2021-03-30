
def wrap(string,max_width):
	L=[]
	for i in range(0,len(string),max_width):
		L.append(string[i:i+max_width])
	s="\n".join(L)
	return s
