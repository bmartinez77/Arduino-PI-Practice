#!/usr/bin/env python3
import serial
import time

while True:
    try: 
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
        print("Successfully connected Serial.")
        break
    except serial.SerialException:
        print("Could not connect to Serial. Try again.")       
        time.sleep(1)
    
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK")

try:
    while True:
        time.sleep(1)
        message = input("Type 'on' or 'off' !\n")
        pre = "This is the message sent: "
        print(pre + message)
        message = message +"\n"
        ser.write(message.encode('utf-8'))
        
except KeyboardInterrupt:
    print("Close Serial Communication.")
    ser.close()    