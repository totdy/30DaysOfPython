from datetime import *

#1
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
#2
print(now.strftime("%m/%d/%Y, %H:%M:%S"))
#3
print(datetime.strptime('5 December, 2019', '%d %B, %Y'))
#4
nexYear = datetime(year + 1, 1, 1, hour, minute)
print('{} to next year'.format(nexYear - now))
#5
print('{} from year 1970'.format(now - datetime(1970, 1, 1, 0, 0, 0, 0)))