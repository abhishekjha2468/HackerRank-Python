from collections import Counter
L=[]
for i in range(int(input())): L.append(input())
print(len(set(L)))
print(*map(lambda x: f'{x}', (Counter(L)).values()),end=" ")