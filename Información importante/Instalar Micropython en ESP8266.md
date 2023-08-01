### Se requiere tener "esptool.py" y python instalado

1. esptool.py --port COMX erase_flash
2. cd Downloads
3. esptool.py --port COMX --baud 115200 write_flash --flash_size=detect 0 esp8266-20230426-v1.20.0.bin

<h4 style="color:orange;"> Recordar cambiar la ultima parte por la versión más actualizada de Micropython para el esp8266. La puedes encontrar en el siguiente enlace:</h4>

http://micropython.org/download/esp8266/