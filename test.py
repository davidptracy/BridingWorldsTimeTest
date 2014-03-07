"""letting my environment know the path profile for python"""
#!/usr/bin/sh

import time
import datetime


time.timezone = -5.00
current_time = int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')))
output_time = int(time.mktime(time.strptime('2014-03-04 11:00:00', '%Y-%m-%d %H:%M:%S')))
event_Time = output_time - time.timezone

delta = event_Time - current_time

print(delta)
