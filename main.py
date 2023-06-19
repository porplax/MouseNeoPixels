import serial
import pyautogui
import time
import json

ser = serial.Serial(
    '/dev/ttyACM0',
    baudrate=115200,
    timeout=0.05,
    write_timeout=1)

while True:
    try:
        ser.write(json.dumps({"x": pyautogui.position()[0]}).encode())
        ser.write(b"\r\n")
    except serial.serialutil.SerialTimeoutException:
        print('Hang!')
    time.sleep(0.010)
