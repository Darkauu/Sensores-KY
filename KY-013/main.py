#Código para leer temperatura

import machine
import time
import math
# Definir el pin de entrada analógico
analog_pin = machine.ADC(0)


# Función para convertir la lectura analógica a temperatura en grados Celsius
def obtener_temperatura():
    lectura_analogica = analog_pin.read()
    voltaje = lectura_analogica * 3.3 / 1024  # Convertir la lectura a voltaje (valor 0-3.3V)
    resistencia = (3.3 * 10e3 - voltaje * 10e3) / voltaje  # Calcular resistencia del termistor
    temperatura = 1 / (
                (1 / 298.15) + (1 / 3435) * (math.log(resistencia / 10e3))) - 273.15  # Calcular temperatura en °C
    return temperatura

# Bucle principal
while True:
    temperatura_actual = obtener_temperatura()

    # Verificar si la temperatura está dentro del rango permitido
    if temperatura_actual >= -55 and temperatura_actual <= 125:
        print("Temperatura: %.2f °C" % temperatura_actual)
    else:
        print("Temperatura fuera de rango")

    time.sleep(1)  # Esperar 1 segundo antes de tomar la siguiente lectura
