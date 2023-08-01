#Código que ejecuta 8 frecuencias en forma ascendente

from machine import Pin, PWM
import time
notes = [440, 510, 570, 630, 700, 780, 840, 900]

buzzer_pin = PWM(Pin(14))  # Pin de conexión del buzzer

for i in notes:
    buzzer_pin.freq(i)  # Establecer la frecuencia en 1000 Hz
    buzzer_pin.duty(512)  # Establecer el ciclo de trabajo al 50% (valor entre 0 y 1023)
    time.sleep(0.5)  # Duración del tono (200 ms)