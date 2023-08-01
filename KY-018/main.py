import machine
import time

# Configuración del pin analógico
adc = machine.ADC(0)  # Usamos el pin analógico A0 (cambio el número si usas otro pin)

while True:
    # Leer el valor analógico
    valor_analogico = adc.read()

    # Convertir el valor analógico a un rango de 0 a 100 (invertido)
    porcentaje_luz = int((1023 - valor_analogico) * 100 / 1023)

    # Imprimir el porcentaje de luz
    print("Porcentaje de luz: ", porcentaje_luz)

    # Pausa entre lecturas
    time.sleep(1)  # Pausa de 1 segundo (ajusta el tiempo según tus necesidades)
