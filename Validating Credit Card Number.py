def count(string):
	string=string
	Count=1
	list=[]
	for i in range(len(string)):
		try:
			if i<(len(string)-1):
				if string[i]==string[i+1]:
					Count=Count+1
				else:
					list.append(Count)
					Count=1
			else:
				list.append(Count)
		except:
			list.append(Count)
	return max(list)
#----------------------------------------
	
if __name__=='__main__':
	n=int(input())
	for m in range(n):
		num=list(input())
		#print(num)
		N=[]
		flag='Invalid'
		c=True
		while(c):
			try:
				if int(num[0]) not in [4,5,6]:
					#print('Goes Wrong in line no.. 10')
					c=False
					break
				#print("First Condition in passed That first number is either 4,5 or 6")
				if len(num)==16:
					new=[ int(i) for i in num ]
					#print("While Checking integer ")
					#print("new num list is: ",new)
					#set_list=list(set(new))
					#print("All Good Till line finding unique number in num list i.e : ",set_list)
					if count(''.join(num))>3:
						c=False
						break
					#for i in set_list:
							#print("Checking the count of ",i)
							#if new.count(i)>=4:
								 #N.append(new.count(i))
								 #print("Error on counting")
								# c=False
								 #break
					#print("The Highest Count is ",N)
					if len(new)==16 and N==[]:
						flag='Valid'
						#print("Flag is set to Valid")
						#print("Breaking the while loop now ")
						c=False	
						break
				#-------------------------------------------------
				elif len(num)==19 and num.count('-')==3:
					#print("we are on secound case of hyphen '-' ")
					h=[]
					h.append(num.pop(4))
					h.append(num.pop(8))
					h.append(num.pop(12))
					#print("hyphen list is: ",h)
					if h!=['-','-','-']:
						c=False
						break
					else: continue
					#print("All hyphen are on right position ")
					new=[ int(i) for i in num ]
					#print("While Checking integer ")
					#print("new num list is: ",new)
					#set_list=list(set(new))
					#print("All Good Till line finding unique number in num list i.e : ",set_list)
					if count(''.join(num))>3:
						c=False
						break
					#for i in set_list:
							#print("Checking the count of ",i)
							#if new.count(i)>=4:
								 #N.append(new.count(i))
								 #print("Error on counting")
								 #c=False
								 #break
					#print("The Highest Count is ",N)
					if len(new)==16 and N==[]:
						flag='Valid'
						#print("Flag is set to Valid")
						#print("Breaking the while loop now ")
				break
			except:
				flag='Invalid'
				break
		#print("Now we are out of the While Loop")
		print(flag)