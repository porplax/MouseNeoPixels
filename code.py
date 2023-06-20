import supervisor
import usb_cdc
import time
import json

import neopixel
import board
import sys
import math
PIXEL_PIN = board.GP16
NUMBER_OF_PIXELS = 30
ORDER = neopixel.GRB

neo = neopixel.NeoPixel(
    PIXEL_PIN, NUMBER_OF_PIXELS, brightness=0.5, auto_write=False, pixel_order=ORDER)
neo.fill((0, 0, 0))
neo.show()
print("listening...")
serial = sys.stdin

offset = -1
height = 0
while True:
    neo.fill((10, 10, 10))
    if supervisor.runtime.serial_bytes_available:
        data_in = serial.readline()
        data = None
        if data_in:
            try:
                data = json.loads(data_in)
            except ValueError:
                data = {"raw": data_in}

        if isinstance(data, dict):
            if "x" in data:
                
                try:
                    neo[int(data["x"]/64)-(2-offset)] = (64, 64, 64)
                    neo[int(data["x"]/64)-(1-offset)] = (127, 127, 127)
                    neo[int(data["x"]/64)+offset] = (255, 255, 255)
                    neo[int(data["x"]/64)+(1+offset)] = (127, 127, 127)
                    neo[int(data["x"]/64)+(2+offset)] = (64, 64, 64)
                except:
                    pass
            if "key" in data:
                try:
                    height = int(data["key"])
                except:
                    pass
    neo.show()

    height += .01
    
    time.sleep(0.001)
