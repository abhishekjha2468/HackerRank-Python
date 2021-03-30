try:
	for i in range(int(input(""))):
		s=[int(i) for i in input("").split(" ")]
		if s[0]>1 and s[1]==1:
			print(-1)
		elif s[0]<s[1]:
			print(-1)
#		elif ((s[0]>=s[1]) and (s[0]<=(s[1]*s[2]))):
		else:
			j=1
			L=[]
			for i in range(s[0]):
				if j>s[1]:
					j=1
				L.append(str(j))
				j=j+1
			S=list(set(L))
			for i in S:
				c=L.count(i)
				if c>s[2]:
					print(-1)
					break
				if i==S[len(S)-1]:
					k=" ".join(L)
					print(k)
					break
	#	elif (s[1]==1 and s[0]>1):
	#		print(-1)
	#	else:
	#		print(-1)
except:
	pass