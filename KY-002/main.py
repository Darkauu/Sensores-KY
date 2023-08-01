#Código para imprimir un mensaje al detectar una vibración.

import machine
import time

sensor_pin = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)

def vibracion_detectada(pin):
    print("¡Vibración detectada!")

sensor_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=vibracion_detectada)

while True:

    time.sleep(1)
