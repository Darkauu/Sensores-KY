
### Puntos Importantes:

-Interfaz analógica: El KY-001 proporciona una salida analógica proporcional a la temperatura medida.

-Rango de temperatura: El rango de temperatura medible depende del termistor específico utilizado en el módulo KY-001. Generalmente, el rango de temperatura puede variar de -55 °C a +125 °C.

-Precisión: La precisión del módulo KY-001 puede depender tanto del termistor utilizado como de la calidad del circuito de interfaz analógica. Sin embargo, en general, estos módulos no ofrecen una alta precisión en comparación con sensores de temperatura más especializados.

-Aplicaciones: El KY-001 puede ser utilizado en diversas aplicaciones como: Monitoreo de temperatura ambiente, Control de temperatura de sistemas, Proyectos de domótica o registro de datos, Automatización de agrícola, etc.

---
### ¿Cómo funciona?

Es un módulo de sensor de temperatura basado en el termistor NTC (Coeficiente de Temperatura Negativo). Está diseñado para medir la temperatura ambiente y proporcionar una señal de salida analógica proporcional a la temperatura medida.

El módulo KY-001 utiliza un chip de interfaz analógica AD22100 para amplificar y convertir la señal del termistor en una señal de voltaje que puede ser fácilmente leída por un microcontrolador o un Arduino. Tiene tres pines: VCC para la alimentación, GND para la conexión a tierra y OUT para la salida analógica.

Para utilizar el módulo KY-001, generalmente debes conectar el pin VCC a una fuente de alimentación de 5V, el pin GND a la tierra del sistema y el pin OUT a una entrada analógica(En el caso del ESP8266 es A0) 

---
### Problemas encontrados/Comentarios:

- Aveces el **ds18x20** no es reconocido por Pycharm. 
- Aveces el **onewire** no es reconocido por Pycharm.