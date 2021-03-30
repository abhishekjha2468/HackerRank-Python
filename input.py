a=[int(i) for i in input().split()]
b=input().replace(' ','')
x=a[0]
y=a[1]
t=0
num=x
i=1
while(i<len(b)):
	if '**'==b[i:i+2]:
#		print("Applying ** opertaion")
		t=t+(num**int(b[i+2]))
#		print("t is ",t)
		i=i+3
#		print(f'Now i is {i} and len of string is {len(b)}')
		if i==len(b):
			break
	elif '*'==b[i]:
#		print(f"* is compared to b[{i}] i.e ",b[i])
#		print("Applying * opertaion")
		t=t+num*int(b[i+1])
#		print("t is ",t)
		i=i+2
#		print(f'Now i is {i} and len of string is {len(b)}')
		if i==len(b):
			break
	elif '/'==b[i]:
#		print(f"/ is compared to b[{i}] i.e ",b[i])
#		print("Applying / opertaion")
		t=t+(num/int(b[i+1]))
#		print("t is ",t)
		i=i+2
#		print(f'Now i is {i} and len of string is {len(b)}')
		if i==len(b):
			break
	elif '+'==b[i] and b[i+1]!="x":
#		print("Applying + operation")
		t=t+int(b[i+1])
#		print("t is ",t)
		i=i+2
#		print(f'Now i is {i} and len of string is {len(b)}')
		if i==len(b):
			break
	elif '-'==b[i] and b[i+1]!="x":
#		print("Applying - operation")
		t=t-int(b[i+1])
#		print("t is ",t)
		i=i+2
#		print(f'Now i is {i} and len of string is {len(b)}')
		if i==len(b):
			break
	elif '+'==b[i] and ('+'==b[i+2] or '-'==b[i+2]):
		t=t+num
		i=i+1
		if i==len(b):
			break
	elif '-'==b[i] and ('+'==b[i+2] or '-'==b[i+2]):
		t=t-num
		i=i+1
		if i==len(b):
			break
	else:
		i=i+1
		pass
print(t==y)