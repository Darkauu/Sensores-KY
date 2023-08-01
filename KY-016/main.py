#Código para color rosado

import machine
import time

pin_R = machine.PWM(machine.Pin(12))
pin_G = machine.PWM(machine.Pin(13))
pin_B = machine.PWM(machine.Pin(14))

pin_R.freq(1000)
pin_G.freq(1000)
pin_B.freq(1000)

def set_rgb_color(blue, green, red):
    pin_R.duty(blue)
    pin_G.duty(green)
    pin_B.duty(red)

while True:
    set_rgb_color(400, 0, 900)
    time.sleep(1)