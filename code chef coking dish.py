try:
	for _ in range(int(input())):
		a,time=int(input()),[*map(int,input().split())]
		time.sort()
	#	print("Sorted time: ",time)
		burner1,burner2=[time.pop()],[]
	#	print("burner1,burner2,time: ", burner1, burner2,time)
		for n in range(len(time)):
			try:
				burner2.append(time.pop())
			except: break
			try:
				burner2.append(time.pop())
			except: break
			try:
				burner1.append(time.pop())
			except: break
			try:
				burner1.append(time.pop())
			except: break
	#	print(burner1,burner2)
		print(max(sum(burner1),sum(burner2)))
except: pass