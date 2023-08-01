### Estos son inconvenientes que podrían ocurrir utilizando el ESP8266 con Micropython:

1. Siempre se debe utilizar un file con el nombre de "main.py" al cargar un código a un ESP8266 (Se asume que al ESP32 también)


2. Si su computadora no reconoce su puerto COMX, aún si cada parámetro y configuración están correctamente instaladas, trate borrando el flash del ESP8266 y volviendo a instalar el Micropython


3. Si un código no está funcionando correctamente, aún si toda la sintaxis y configuraciones estén correctas, revisar que los pines estén correctamente conectados y cambiar de pines digital (Ejemplo: Cambiar de GPIO3 a GPIO15)


4. Revisar la conexión de los pines, algúnas veces los fabricantes no marcan correctamente los pines y sus posiciones. Algunos datos son:<br><br>
	-En los sensores de 3 pines, el central siempre será el VCC<br>
   
	-En la mayoría de casos, los sensores que no sean LED, van a necesitar conectarse siempre 2 pines escenciales: GND(pin de 	tierra) y VCC(pin de alimentación)<br>
   
	-Comprobar que el cable jumper funcione correctamente y se sienta cierta presion al conectarlo


5. El ESP8266 tiene únicamente un ADC(pin analógico(A0))


6. Cuando se toman valores leídos de un pin ADC pueden dar valores muy altos o que no corresponden a lo que se está midiendo. En ese caso, probar utilizando la siguiente formula: valor_leido=(valor_leido*100)/1023. 

Esto es debido a que los pines analógicos generalmente tienen una resolución de 10 bits. Esto significa que el ADC (convertidor analógico a digital) puede representar valores en un rango de 0 a 1023 (2^10 - 1), donde 0 representa el valor mínimo y 1023 representa el valor máximo.

En estas situaciones, puedes ajustar la escala de los datos multiplicando el valor leído por un factor adecuado y dividiéndolo por la resolución máxima (1023). En el caso mencionado de multiplicar por 100 y dividir por 1023, se logra una escala proporcional en el rango de 0 a 100.