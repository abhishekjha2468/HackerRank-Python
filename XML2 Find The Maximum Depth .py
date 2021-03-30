import re
list=[ input() for i in range(int(input())) ]
depth=[]
for string in list: depth.append(int((re.search(r'\S', string).start())/4))
print(max(depth))
'''