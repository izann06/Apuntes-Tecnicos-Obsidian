
> La invención más importante del siglo XX. Todo lo demás se construye sobre esta base.

---
## ¿Qué es un transistor?

Un transistor es un **interruptor microscópico sin piezas móviles** fabricado con silicio dopado. Inventado en 1947 por John Bardeen, Walter Brattain y William Shockley en los laboratorios Bell, les valió el Premio Nobel de Física en 1956.

A diferencia del interruptor de la luz de tu habitación (que tiene una palanca física que mueves con la mano), el transistor **se controla con electricidad**: una pequeña corriente en una entrada decide si la corriente principal puede pasar o no. Si hay corriente abrimos la entrada (1) si no hay la cerramos (0).

El transistor es el invento moderno más importante,gracias a el tenemos todo tipo de aparatos eléctricos como: Wi-Fi, Neveras, Microondas, Móviles, Altavoces, Micrófonos, Ordenadores...

> [!NOTE] Curiosidad del Microondas
> El tema del microondas es interesante porque para calentar la comida usa una pieza que se llama `Magnetrón` que es una válvula de vacío y no se usan transistores ahí porque a nivel de potencia y económico no sale rentable.
> 
> Un magnetrón de 10 centímetros puede escupir **1.000 Vatios (W)** de potencia
> 
> El problema es que el magnetrón es digital o calienta al 100% o no calienta 0%, cuando bajas la temperatura por ejemplo 50% lo que hace el magnetrón es básicamente se enciende un tiempo y el otro tiempo se apaga. Con los transistores analógicos si se podría hacer eso.
> 


---

## ¿Cómo funciona? (sin cerebro, solo física)

El transistor no tiene inteligencia. No decide nada. Solo responde a la física del silicio dopado.

Tiene tres terminales:

- **Colector / Drenador (Drain)**: por donde entra la corriente principal.

- **Base / Puerta (Gate)**: Es el que decide si pasa la corriente o no;es como una válvula,la llave del grifo.

- **Emisor / Fuente (Source)**: por donde sale la corriente principal.

![[📄02 - El Transistor.png]]


Si la **Base** está cerrada por mucha corriente que haya no pasa:
![[📄02 - El Transistor-1.png|697]]

Si la **Base** está abierta,la corriente pasa:
![[📄02 - El Transistor-2.png]]

### Analogía de la manguera (Ejemplo por si no lo entiendes)

Imagina una manguera de jardín con el pie encima:

- **Pie encima → agua bloqueada**: equivale a no aplicar voltaje a la base → el silicio actúa como aislante → la corriente no pasa → **estado 0**.

- **Pie levantado → agua fluye**: equivale a aplicar un pequeño voltaje a la base → la unión PN del silicio se vuelve conductora → la corriente principal pasa → **estado 1**.

La física exacta: al aplicar voltaje a la base se crea un campo eléctrico que permite a los electrones cruzar la unión PN que normalmente los bloqueaba. No hay palancas, no hay decisiones, solo física de materiales.

---

## ¿Por qué no necesita "saber" nada el transistor?

Es una pregunta muy buena. El transistor no interpreta el voltaje que recibe. Simplemente, por la naturaleza del silicio dopado:

- Por debajo de un umbral de voltaje (~0.7V en silicio): aislante → 0.

- Por encima de ese umbral: conductor → 1.

Es tan "tonto" como una esponja que absorbe agua si la metes en un cubo y no absorbe si no lo haces. La esponja no decide, solo responde a la física.

---

## ¿Cuántos transistores hay en un procesador?

|Año|Procesador|Transistores|
|---|---|---|
|1971|Intel 4004|2.300|
|1989|Intel 486|1.000.000|
|2006|Intel Core 2|291.000.000|
|2023|Apple M2 Ultra|134.000.000.000|

Los transistores modernos tienen un tamaño de entre 3 y 7 nanómetros (un nanómetro es la millonésima parte de un milímetro). Son tan pequeños que unos 10.000 caben en la anchura de un cabello humano.

---

## Los GHz: el reloj del procesador(REVISAR EN GEMINI)

Los GHz (Gigahercios) no miden la velocidad exacta de cada operación, sino la **frecuencia del reloj** del procesador, es decir, cuántas veces por segundo el procesador sincroniza sus operaciones.

- 1 Hercio (Hz) = 1 ciclo por segundo.

- 1 GHz = 1.000.000.000 ciclos por segundo.

En cada ciclo de reloj, el procesador puede ejecutar una o varias instrucciones (dependiendo de la arquitectura). Un procesador a 3.5 GHz está "marcando el ritmo" 3.500 millones de veces cada segundo.

### ¿Por qué se calientan?

Cada vez que un transistor cambia de estado (de 0 a 1 o de 1 a 0), consume energía y disipa calor. Con miles de millones de transistores cambiando de estado miles de millones de veces por segundo, la cantidad de calor generado es enorme. Por eso los procesadores necesitan ventiladores, disipadores o refrigeración líquida.

### ¿Más GHz = más rápido siempre?

No necesariamente. Un procesador puede hacer más trabajo por ciclo (más instrucciones por ciclo, IPC) o puede tener más núcleos trabajando en paralelo. Por eso un procesador moderno a 3.5 GHz puede ser mucho más potente que uno antiguo a 4 GHz.

---

## Historia y evolución

| Generación | Tecnología | Tamaño |
| ---------- | ----------------------- | ------------------ |
| 1947 | Transistor de germanio | Varios centímetros |
| 1960s | Transistor de silicio | Milímetros |
| 1970s | Circuitos integrados | Micrómetros |
| 1990s | MOSFET submicrónico | Cientos de nm |
| 2020s | FinFET, Gate-All-Around | 3-5 nm |

---

## Siguiente paso

[[03 - Semiconductores Avanzados]] → el silicio no es el único semiconductor: GaAs, GaN, SiC e InP para aplicaciones especializadas.

O salta a [[04 - Puertas Lógicas y ALU]] para ver cómo los transistores se combinan para crear lógica.