import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
timestamp_hour =int( time.strftime('%H'))
print(timestamp_hour)
timestamp =int( time.strftime('%M'))
print(timestamp)
timestamp =int( time.strftime('%S'))
print(timestamp)
if timestamp_hour < 12:
     print('Good morning')
elif timestamp_hour <18:
    print('Good afternoon')
else:
    print('Good evening')