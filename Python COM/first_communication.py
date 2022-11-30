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
        print("Send message to Arduino")
        ser.write("Hello from Pi\n".encode('utf-8'))
        while ser.in_waiting <= 0:
            time.sleep(0.01)
        response = ser.readline().decode('utf-8').rstrip()
        print(response)
except KeyboardInterrupt:
    print("Close Serial Communication.")
    ser.close()




# Read data from arduino
      #if ser.in_waiting > 0:
        #    line = ser.readline().decode('utf-8').rstrip()
        #    print(line)