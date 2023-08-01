#Código que dispare un laser intermitentemente

import machine
import time

laser_pin = machine.Pin(15, machine.Pin.OUT)

while True:
    laser_pin.on()
    time.sleep(0.2)
    laser_pin.off()
    time.sleep(0.2)