for i in range(int(input())):
	try:
		f=str(input())
		print((type(float(f))==float) and f[-1]!='.' and ('.' in f))
	except: print(False)