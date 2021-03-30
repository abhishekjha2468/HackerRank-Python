import re
pattern=r'([a-z0-9]+[_a-z0-9\.-]*[a-z0-9]+)@([a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{,3})'
for _ in range(int(input())):
	text=input()
	if len(re.findall(pattern,text)) == 1:
		print(text)