#Código de inclinación

import machine

# Configurar el pin GPIO del ESP8266 para el sensor KY-020
sensor_pin = machine.Pin(4, machine.Pin.IN)  # Pin GPIO4 para la señal del sensor KY-020

# Función para leer el estado de inclinación
def leer_inclinacion():
    return sensor_pin.value()

# Loop principal
while True:
    inclinacion = leer_inclinacion()

    if inclinacion == 1:
        # El sensor está inclinado
        print("El sensor está inclinado.")
    else:
        # El sensor no está inclinado
        print("El sensor no está inclinado.")
