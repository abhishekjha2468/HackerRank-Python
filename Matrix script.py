import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(list(matrix_item))
s=[]
for i in list(zip(*matrix)):
	s.append("".join(i))
#print("".join(s))
f="".join(s)
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", f))