i=int(input(""))
L=[]
for i in range (0,i):
	string=input("")
	v={'9','8','7'}
	f={string[0]}
	if (len(v-f)==2) and (len(string)==10):
		L.append("YES")
	else:
		L.append("NO")
for i in L:
	print(i)

		