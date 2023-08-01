### Instalar Micropython para ejecutar códigos a microcontroladores

1. Crea un nuevo proyecto 


2. Ir a File > Settings > Plugins > Buscar "MicroPython" en el Marketplace


3. Conecta tu Microcontrolador a tu ordenador


4. Ir a File > Settings > Languages & Frameworks


5. Pulsar "Enable MicroPython support", seleccionar el tipo de despositivo (ESP8266 por ejemplo)


6. En Device path escribir o detectar el puerto COMX asignado a tu microcontrolador y presionar Apply.


7. Ir a File > Settings > Project:proyect_name > Project Structure y excluye la carpeta de .idea y venv presionando clickderecho sobre ellas.


8. Crea un archivo "<b>.py</b>" dentro de tu proyecto e instala los paquetes que te sugiere Pycharm 


9. Ir a Tools > MicroPython > MicroPython REPL

**Recordar aplicar la configuración establecida en la parte superior derecha de Pycharm**