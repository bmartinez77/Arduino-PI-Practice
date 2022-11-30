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
        if ser.in_waiting > 0:
            num = int(ser.readline().decode('utf-8').rstrip())
        
            print(num)
            if num > 15:
                print("LIGHT is ON")
                ser.write("on\n".encode('utf-8'))
            else:
                print("LIGHT is OFF")
                ser.write("off\n".encode('utf-8'))
            
            

        
except KeyboardInterrupt:
    print("Close Serial Communication.")
    ser.close()    
