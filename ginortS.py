a=[ i for i in input()]
#print("a is: ",a)
char_lower=[]
char_upper=[]
odd_number=[]
even_number=[]
for i in a:
	try:
		if int(i)==int(i):
			if int(i)%2==0:
				even_number.append(i)
			else: odd_number.append(i)
	except:
		if i.lower()==i:
			char_lower.append(i)
		elif i.upper()==i:
			char_upper.append(i)
	char_lower.sort()
	char_upper.sort()
	odd_number.sort()
	even_number.sort()
#print("sorted char_lower: ",char_lower)
#print("sorted char_upper: ",char_upper)
#print("sorted odd_number: ",odd_number)
#print("sorted even_number: ",even_number)
list=char_lower+char_upper+odd_number+even_number
print(''.join(list))