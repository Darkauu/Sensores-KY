### Puntos importantes
-Funcionalidad: El KY-016 es un módulo que contiene un LED RGB (rojo, verde, azul) en un solo paquete. Permite controlar la intensidad de cada color primario para generar una amplia gama de colores.

-Voltaje de funcionamiento: El KY-016 generalmente opera con un voltaje de 5V

-Conexión: Generalmente tiene tres pines de conexión: R (rojo), G (verde) y B (azul). Estos pines se conectan a los pines de salida PWM (Modulación por Ancho de Pulso) de un microcontrolador para controlar la intensidad de cada color.

---
### ¿Cómo funciona?

el KY-016 es un módulo de sensor de LED RGB. Este módulo se utiliza para detectar la intensidad de luz en diferentes colores y generalmente se utiliza en proyectos relacionados con la iluminación y la detección de colores.

El módulo KY-016 normalmente viene con un LED RGB y un fototransistor. El LED RGB puede emitir diferentes colores de luz, mientras que el fototransistor detecta la intensidad de la luz reflejada por la superficie cercana al sensor.

Este tipo de sensor puede ser utilizado en proyectos de automatización de iluminación, robótica, diseño de interiores y otros proyectos creativos donde se requiere la detección y control de colores de luz.


---
### Problemas encontrados/Comentarios

- Para graduar cada led en la función "set_rgb_color()" los parametros serían (R, G, B)
- La graduación de color va de 0 a 1023