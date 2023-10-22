import serial
import time
import datetime
import os

old_temp = 24.0
low_pass_gain = 0

def low_pass_filter(old_val,val,k):
    return (old_val * k) + (val * (1 - k))

def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True
    
time_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(time_delta,'JST')
NOW = datetime.datetime.now(JST)
DATE_STR = NOW.strftime("%Y-%m-%d-%H%M%S")
TIME_STR = NOW.strftime("%H:%M:%S")
 
FileName_withdate = './log/' + DATE_STR + '_templog.txt'

templog_file = open(FileName_withdate,'w')

arduino_serial = serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=0.1)

while True:
    templog_file = open(FileName_withdate,'w')
    temp = arduino_serial.readline()
    utf_temp = temp.decode('utf-8')
    if utf_temp == '999':
        break
    else:
        utf_temp = temp.decode('utf-8')
        if is_num(utf_temp) == True:
            temp_f = low_pass_filter(float(old_temp),float(utf_temp),low_pass_gain)
            print(TIME_STR + ',' + str(temp_f))
            templog_file.write(str(temp_f) + '\n')
            old_temp = temp_f


arduino_serial.close()
templog_file.close()
print("complete! templog file was seved")