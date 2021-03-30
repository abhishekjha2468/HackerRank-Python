import re
text="Hello  1234 1+@)-£# "
for i in range(int(input())):
	try:
		i=input()
		re.search(r'{}'.format(i),text)
		print(True)
	except:
		print(False)