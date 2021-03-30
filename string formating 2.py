def print_formatted(i):
	l=len("{0:b}".format(i))
	for a in range (1,i+1):
		print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(a,w=l))