cube = lambda x:x*x*x
def fib(n):
	if n==1 or n==0:
		return n
	else:
		return fib(n-1)+fib(n-2)
def fibonacci(n):
	L=[]
	for i in range(0,n):
		L.append(fib(i))
	return L
