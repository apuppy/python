from datetime import datetime
now = datetime.now()
#print(now)
# year month day
year = now.year
month = now.month
day = now.day

print("current year %s,current month %s,today is %s" % (year,month,day) )

#format the datetime
print("Today is %s-%s-%s" % (year,month,day) )

hour = now.hour
minute = now.minute
second = now.second

print("Time now : %s:%s:%s" % (hour,minute,second) )

#print datetime together
print ('%s-%s-%s %s:%s:%s' % (now.year,now.month,now.day,now.hour, now.minute, now.second) )

print(now.timestamp())