#Código que dectecte cuando hay y cuando no hay un objeto

from machine import Pin
import time

# Configura el pin de entrada
entrada_pin = Pin(4, Pin.IN)  # Cambia el número de pin según tu configuración

# Bucle principal
while True:
    estado = entrada_pin.value()  # Lee el estado del pin de entrada

    if estado:
        print("Objeto detectado")
        time.sleep(1.5)
    else:
        print("Sin objeto")
        time.sleep(1.5)
