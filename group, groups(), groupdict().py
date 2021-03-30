import re
a=re.search(r'([0-9]|[a-z]|[A-Z])\1+',input())
print(a.group(1) if a!=None else -1)