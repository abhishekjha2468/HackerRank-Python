i=int(input(""))
L=[]
for i in range (0,i):
	string=input("")
	s=set(string)
	string1="abcdefghijklmnopqrstuvwxyz"
	a=set(string1)
	string2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	A=set(string2)
	v={'9','8','7'}	
	f={string[0]}
	if len(a-s)<26 or len(A-s)<26:
		L.append("NO")
	elif (len(v-f)==2) and (len(string)==10):
		L.append("YES")
	elif (len(v-f)!=2) or (len(string)!=10):
		L.append("NO")
for i in L:
	print(i)

		