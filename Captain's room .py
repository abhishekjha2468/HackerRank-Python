from collections import Counter
n=int(input())
list=input().split()
x, y = Counter(list).most_common()[-1]
print(x)