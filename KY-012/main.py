#Código que te pide introducir la frecuencia con la que vibra y el tiempo de duración en milisegundos

from machine import Pin, PWM
import time

# Configura el pin de salida para controlar el buzzer
buzzer_pin = Pin(5, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)

# Genera un tono con una frecuencia específica y duración
def play_tone(frequency, duration):
    buzzer_pwm.freq(frequency)
    buzzer_pwm.duty(512)
    time.sleep_ms(duration)
    buzzer_pwm.duty(0)

# Frecuencia y duración del tono
tone_frequency = int(input("Frecuencia en Hz: "))  # Frecuencia en Hz
tone_duration = int(input("Duración en ms: "))   # Duración en milisegundos

# Genera el tono
play_tone(tone_frequency, tone_duration)

# Apaga el buzzer al finalizar
buzzer_pwm.deinit()
