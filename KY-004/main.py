#Código que muestre un mensaje al presionar y liberar el botón

import machine

# Configura el pin del botón
button_pin = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

# Función de interrupción para manejar el cambio de estado del botón
def button_interrupt(pin):
    if pin.value() == 0:
        print("¡Botón presionado!")
    else:
        print("¡Botón liberado!")

# Configura la interrupción en el pin del botón
button_pin.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=button_interrupt)

while True:
    pass
