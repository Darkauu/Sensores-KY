#Código que envie una señal infrarroja

import machine
import time

# Configuración de pines
ir_led_pin = machine.Pin(14, machine.Pin.OUT)  # GPIO14 en ESP8266

# Función para enviar una señal infrarroja
def enviar_infrarrojo():
    # Encender el LED infrarrojo durante un tiempo determinado
    ir_led_pin.on()
    time.sleep(100)  # Duración de la señal (ajusta según tus necesidades)
    ir_led_pin.off()

# Bucle principal
while True:
    enviar_infrarrojo()
    time.sleep(1)  # Esperar 1 segundo antes de enviar otra señal

