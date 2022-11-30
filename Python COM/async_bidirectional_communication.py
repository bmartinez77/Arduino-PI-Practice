#!/usr/bin/env python3
import serial
import time

last_time_reset_counter = time.time()
reset_counter_delay = 10.0

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
        time_now = time.time()
        if time_now - last_time_reset_counter >= reset_counter_delay:
            last_time_reset_counter = time_now
            print("Reseting count")
            ser.write("reset\n".encode('utf-8'))
        
        if ser.in_waiting > 0:
            counter = int(ser.readline().decode('utf-8').rstrip())
            print("Recieved count: " + str(counter))    
     
    
                   
except KeyboardInterrupt:
    print("Close Serial Communication.")
    ser.close()   