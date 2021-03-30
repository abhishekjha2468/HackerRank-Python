import calendar
day=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
Date=[int(i) for i in input().split()]
y=Date[2]
m=Date[0]
d=Date[1]
print(day[calendar.weekday(y,m,d)])