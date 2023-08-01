#Código de efecto fade

from machine import Pin, PWM
import time

# Se configuran los pines de salida para el control del LED RGB
redPIN = Pin(12, Pin.OUT)
greenPIN = Pin(13, Pin.OUT)
bluePIN = Pin(14, Pin.OUT)

# Se asignan las variables de los pines, a variables PWM para controlarlos
pwm_r = PWM(redPIN)
pwm_g = PWM(greenPIN)
pwm_b = PWM(bluePIN)

# Configurar la frecuencia de PWM (ajustable según tus necesidades)
pwm_r.freq(2000)
pwm_g.freq(2000)
pwm_b.freq(2000)

# Función para establecer el color del LED RGB con fundido suave
def fade_color(target_red, target_green, target_blue, fade_time):
    # Obtener los valores de color actuales
    current_red = pwm_r.duty() / 1023  # Escala de 0 a 1
    current_green = pwm_g.duty() / 1023  # Escala de 0 a 1
    current_blue = pwm_b.duty() / 1023  # Escala de 0 a 1

    # Calcular la cantidad de cambio por iteración de tiempo
    fade_steps = 100  # Número de pasos de fundido
    time_per_step = fade_time / fade_steps
    red_step = (target_red - current_red) / fade_steps
    green_step = (target_green - current_green) / fade_steps
    blue_step = (target_blue - current_blue) / fade_steps

    # Realizar el fundido suave en incrementos de tiempo
    for step in range(fade_steps):
        # Calcular los nuevos valores de color
        new_red = current_red + (red_step * step)
        new_green = current_green + (green_step * step)
        new_blue = current_blue + (blue_step * step)

        # Establecer el nuevo color del LED RGB
        set_color(new_red, new_green, new_blue)

        # Pausa hasta el siguiente paso de fundido
        time.sleep(time_per_step)

# Función para establecer el color del LED RGB
def set_color(red, green, blue):
    # Ajustar los ciclos de trabajo de los PWM según los valores de color proporcionados
    pwm_r.duty(int(red * 1023))   # Escala de 0 a 1023
    pwm_g.duty(int(green * 1023)) # Escala de 0 a 1023
    pwm_b.duty(int(blue * 1023))  # Escala de 0 a 1023

# Ejemplo: Fundido suave entre rojo, verde y azul
while True:
    fade_color(1, 0, 0, 1)  # Fundido a rojo en 1 segundo
    fade_color(0, 1, 0, 1)  # Fundido a verde en 1 segundo
    fade_color(0, 0, 1, 1)  # Fundido a azul en 1 segundo
