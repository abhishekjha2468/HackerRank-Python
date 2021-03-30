for i in range(int(input())):
	UID=input()
	UID_FORMAT = False
	while(True):
		if len(UID)!=10 : break
		list=UID
		if len(UID)!=len(set(list)): break
		num_list=[]
		upper_char_list=[]
		lower_char_list=[]
		for i in list:
			try:
				num_list.append(int(i))
			except:
				if i.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
					upper_char_list.append(i)
				elif i.lower() in "abcdefghijklmnopqrstuvwxyz":
					lower_char_list.append(i)
		if len(upper_char_list)<2: break
		if len(num_list)<3: break
		if len(upper_char_list) + len(lower_char_list) + len(num_list) != len(list): break
		UID_FORMAT=True
		break
	if UID_FORMAT: print("Valid")
	else: print("Invalid")