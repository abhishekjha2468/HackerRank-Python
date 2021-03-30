a=int(input())
for j in range(0,a):
	L=[str(i) for i in input().split()]
	a=L[0]
	b=L[1]
	try:
 	   print(int(int(a)/int(b)))
	except ZeroDivisionError as e:
		print("Error Code: integer division or modulo by zero")
	except ValueError as v:
		print("Error Code:",v)