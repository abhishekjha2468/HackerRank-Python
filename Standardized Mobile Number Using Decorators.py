def wrapper(l):
	def fun(f):
		l(f'+91 {x[-10:-5]} {x[-5:]}' for x in f)
	return fun