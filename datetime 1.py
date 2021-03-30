import datetime
import math
for j in range(int(input())):
	T=[i for i in input().split()]
	m={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
	t=[i for i in input().split()]
	#print(T,t)
	day1=int(T[1])
	m1=m[T[2]]
	y1=int(T[3])
	hms=[int(i) for i in T[4].split(':')]
	h1=hms[0]
	min1=hms[1]
	sec1=hms[2]
	tz1=int(T[5])
	
	t1=datetime.datetime(y1,m1,day1,h1,min1,sec1)
	#print(t1)
	#----------------
	
	day2=int(t[1])
	m2=m[t[2]]
	y2=int(t[3])
	hms=[int(i) for i in t[4].split(':')]
	h2=hms[0]
	min2=hms[1]
	sec2=hms[2]
	tz2=int(t[5])
	if y2%400==0:
		day2=day2+1
	elif y2%100==0:
		pass
	elif y2%4==0:
		day2=day2+1
	t2=datetime.datetime(y2,m2,day2,h2,min2,sec2)
	
	d=(abs((t1-t2).total_seconds()) + (int((tz2-tz1)/100))*3600 +((((tz2-tz1)/100)-int((tz2-tz1)/100))*6000))
	'''
		print(((t1-t2).total_seconds()))
		print('+')
		print((tz1-tz2)*36)
		print('=') 
	'''
	if d<=0 and y1<=3000 and y2<=3000:
		print(int(d*(-1)))
	elif d>=0 and y1<=3000 and y2<=3000:
		print(int(d))
	else:
		pass