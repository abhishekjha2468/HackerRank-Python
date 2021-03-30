s=input("")
list=list(s)
L=[False,False,False,False,False]
for i in list:
	if i.isalnum():
		L.pop(4)
		L.insert(4,True)
	if i.isalpha():
		L.pop(0)
		L.insert(0,True)
	if i.isdigit():
		L.pop(1)
		L.insert(1,True)
	if i.islower():
		L.pop(2)
		L.insert(2,True)
	if i.isupper():
		L.pop(3)
		L.insert(3,True)
print(L[4])
print(L[0])
print(L[1])
print(L[2])
print(L[3])