#Código que detecte un CEM e imprima un mensaje

import machine

sensor_pin = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)  # Conecta el sensor al pin D2 (GPIO4) del ESP8266
led_pin = machine.Pin(2, machine.Pin.OUT)  # Conecta el LED al pin D4 (GPIO2) del ESP8266

def handle_interrupt(pin):
    print("¡Campo magnético detectado!")
    led_pin.on()  # Enciende el LED

sensor_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)

while True:
    pass  # Mantén el programa en ejecución
