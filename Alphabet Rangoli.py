n=int(input(""))
string="abcdefghijklmnopqrstuvwxyz"
list=(string)
n=n-1
k=n
c=2
LIST=[]
while k>=0:
	List=[]
	for i in range (0,(2*(n+1))-c):
		List.append("-")
	for i in range (n,k-1,-1):
		List.append(list[i])
		if i!=(k):
			List.append("-")
	for i in range (k+1,n+1):
		if(k+1)!=n+1:
			List.append("-")
			List.append(list[i])
	for i in range (0,(2*(n+1))-c):
		List.append("-")
	print("".join(List))
	if k!=0:
		LIST.append("".join(List))
	k=k-1
	c=c+2
for i in range(len(LIST)-1,-1,-1):
	print(LIST[i])