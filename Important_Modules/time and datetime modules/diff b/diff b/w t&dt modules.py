# >>time module: The time module give the details about "unix time" expressed as a floating point number taken to be seconds
# since the Unix epoch.

# Note:Unix time is a system for describing a point in time. It is the number of seconds that have elapsed since the Unix epoch,

# >>datetime module: the datetime module can support many of the same operations, but provides a more object oriented set of
#  types, and also has some limited support for time zones.

import  time
print(time.time())
print(time.localtime(time.time()))#It returns a time with 9 values (year, month, day, hour, min, sec, Week_day, month_day, DS)
print(time.asctime(time.localtime(time.time())))

import datetime
# the datetime module is used to create a date object (yy,m,d,hour,minute,second)
print(datetime.datetime(2020, 4, 4, 3, 24,2))
# we can print the current time and date with the datetime module
print(datetime.datetime.now())
# To get current date, month, year, hour, minute, second
print(datetime.datetime.now().month)
print(datetime.datetime.now().year)
