#Código que muestra la temperatura y humedad relativa

from machine import Pin
import dht
import time

# Configura el pin de datos del sensor
# Crea una instancia del sensor DHT11
sensor = dht.DHT11(Pin(4))  # Cambia DHT11 por DHT22 si estás utilizando ese modelo

# Lee los datos del sensor
while True:
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()

    # Imprime los valores leídos
    print("Temperatura:", temperature, "°C")
    print("Humedad:", humidity, "%")
    time.sleep(2)
