#Código de temperatura ambiente



import machine
import onewire
import ds18x20 #sensor de temperatura
import time

# Configuración del bus OneWire y el sensor DS18B20
ow = onewire.OneWire(machine.Pin(4))  # Conecta el pin DATA del KY-001 al pin GPIO4 (D2) del ESP8266
sensor = ds18x20.DS18X20(ow)

# Escaneo y detección del sensor DS18B20
roms = sensor.scan()  # Escanea los dispositivos conectados al bus OneWire

if len(roms) > 0:
    print("Sensor DS18B20 encontrado:")
    print("Dirección ROM: ", roms[0])
else:
    print("No se detectó el sensor DS18B20")
    while True:  # Si no se detecta el sensor, detiene la ejecución
        pass

# Lectura de la temperatura
temp_anterior = 0

while True:
    sensor.convert_temp()  # Inicia la conversión de la temperatura
    time.sleep_ms(750)  # Espera 750ms para que se complete la conversión

    for rom in roms:
        temp_actual = sensor.read_temp(rom)  # Lee la temperatura del sensor
        print("Temperatura: %.2f °C" % temp_actual)

    time.sleep(1)  # Espera 1 segundo antes de la siguiente lectura

