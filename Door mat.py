list=[int(i) for i in (input("").split())]
n=list[0]
m=list[1]
c=1
List=[]
for i in range (0,int(n/2)):
	dash=int((m/2)-c)
	L=[]
	L.append("-"*dash)
	L.append(".")
	L.append("|.."*i)
	L.append("|")
	L.append("..|"*i)
	L.append(".")
	L.append("-"*dash)
	a=str("".join(L))
	print(a)
	List.append(a)
	c=c+3
print("-"*int((m/2)-3)+"WELCOME"+"-"*int((m/2)-3))
List.reverse()
for i in List:
	print(i)
	