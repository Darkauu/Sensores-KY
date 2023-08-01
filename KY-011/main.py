#Código de encendido y apagado presionando Enter

import machine

# Configurar el pin digital
led_pin = machine.Pin(4, machine.Pin.OUT)

# Función para encender o apagar el LED
def toggle_led(state):
    led_pin.value(state)

# Ciclo para alternar entre los colores
while True:
    intro=input("Enter para encender")
    print("On")
    toggle_led(1)  # Encender el LED (rojo)
    intro=input("Enter para apagar")
    print("Off")
    toggle_led(1)  # Encender el LED (verde)
    toggle_led(0)
