def minion_game(string):
	all_sub_strings=[]
	p1_sub_strings=[]
	p2_sub_strings=[]
	for i in range(len(string)):
		for j in range(i+1,len(string)+1):
			all_sub_strings.append(string[i:j])
	for i in all_sub_strings:
		if i[0].upper() not in ['A','E','I','O','U']:
			p1_sub_strings.append(i)
		else:
			p2_sub_strings.append(i)
	if len(p1_sub_strings)>len(p2_sub_strings):
		print(f'Stuart {len(p1_sub_strings)}')
	else:
		print(f'Kevin {len(p2_sub_strings)}')
#------------------------------------------------
if __name__=='__main__':
	s=input()
	minion_game(s)