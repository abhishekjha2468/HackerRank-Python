n=int(input())
list=input().split()
A=[]
p=0
for i in list:
	try:
		if int(i)==int(i):
			A.append(int(i))
		if i==i[::-1]:
			p=1
	except:
		break
print(len(A)==n and p==1)