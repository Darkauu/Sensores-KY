#Código que detecte tu BPM cada 0.5

import machine
import time

sensor_pin = machine.ADC(0)

while True:
    sensor_value = sensor_pin.read()
    sensor_value=(sensor_value*100)/1023
    sensor_value=round(sensor_value,2)
    print("Sensor Value:", sensor_value)
    time.sleep(0.5)