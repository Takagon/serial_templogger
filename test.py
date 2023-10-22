import serial
import time
import datetime
import os

time_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(time_delta,'JST')
NOW = datetime.datetime.now(JST)
datestr = NOW.strftime("%Y-%m-%d-%H:%M:%S")

FileName_withdate = datestr + '_templog.txt'


print(FileName_withdate)