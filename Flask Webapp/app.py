#!/usr/bin/env python3
import serial
import time
from flask import Flask
from threading import Thread
while True:
    try: 
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
        print("Successfully connected Serial.")
        break
    except serial.SerialException:
        print("Could not connect to Serial. Try again.")       
        time.sleep(1)
    

app = Flask(__name__)

def background_task():
    while True:
        print("Hello World!!")
        

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()
    thread.run() 
    app.run()