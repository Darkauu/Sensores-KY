#Código que muestra un mensaje dependiendo si el sensor está encendido un o apagado

from machine import Pin
import time

# Se define el pin utilizado para el sensor como entrada
sensor_pin = Pin(5, Pin.IN)

while True:
    # Se obtiene el estado del sensor
    sensor_state = sensor_pin.value()

    # Comprobación del estado del sensor y se imprime el resultado
    if sensor_state == 1:
        print("Apagado")  # Si el sensor está en estado alto, se imprime "Apagado"
    else:
        print("Encendido")  # Si el sensor está en estado bajo, se imprime "Encendido"