
> Antes de que existieran los transistores, había matemáticos que diseñaron el plano teórico de cómo debía funcionar un ordenador.

---

## Alan Turing y la Máquina de Turing (1936)

### ¿Quién era Turing?

Alan Turing (1912-1954) fue un matemático y lógico británico. Es famoso en la cultura popular por liderar el equipo que descifró Enigma (la máquina de cifrado nazi) durante la Segunda Guerra Mundial, lo que según los historiadores acortó la guerra varios años. Pero su contribución más profunda a la humanidad es teórica y anterior a la guerra.

### El problema que intentaba resolver

En los años 30, los matemáticos discutían una pregunta filosófica: ¿existe algún procedimiento mecánico que pueda resolver cualquier problema matemático? ¿O hay problemas que son fundamentalmente irresolubles?

Para responder esto, Turing necesitaba una definición precisa de qué significa "calcular algo" o "seguir un procedimiento". Y lo hizo inventando un modelo abstracto.

### La Máquina de Turing (experimento mental)

No es una máquina física. Es un modelo conceptual, como un experimento de pensamiento matemático.

**Componentes:**

- Una **cinta infinita** dividida en casillas, cada una puede contener un símbolo (por ejemplo, 0, 1 o un espacio en blanco).

- Una **cabeza lectora/escritora** que puede leer el símbolo de la casilla actual, borrar o escribir un nuevo símbolo, y moverse una casilla hacia la izquierda o la derecha.

- Un **estado interno** (como la "memoria de corto plazo" de la máquina). La máquina puede estar en distintos estados, y el estado actual junto con el símbolo leído determinan la acción siguiente.

- Una **tabla de reglas** (el "programa"): si estoy en el estado X y leo el símbolo Y, entonces escribe Z, muévete en dirección D y pasa al estado W.

**Ejemplo muy simplificado:**

Imagina que la cinta tiene el número `1011` (11 en decimal) y queremos sumarle 1.

La máquina seguirá reglas como:

- Si lees un 1 y no hay acarreo: escribe 1, avanza, continúa.

- Si lees un 1 y hay acarreo: escribe 0, propaga el acarreo.

- Si lees un 0 y hay acarreo: escribe 1, no hay más acarreo.
-...

Con reglas suficientemente elaboradas, una Máquina de Turing puede sumar, restar, multiplicar, ordenar listas, reproducir texto, ejecutar cualquier algoritmo que puedas imaginar.

### ¿Por qué es tan importante?

**Punto 1: Definió qué es un algoritmo.** Antes de Turing no había una definición matemática precisa de "procedimiento". La Máquina de Turing la proporcionó.

**Punto 2: Demostró que una sola máquina puede hacerlo todo.** Turing describió la **Máquina de Turing Universal**: una Máquina de Turing que puede leer la descripción de cualquier otra Máquina de Turing y simularla. Esto es exactamente el concepto de un ordenador de propósito general: una máquina que, cambiando las instrucciones (el programa), puede hacer cualquier cosa.

**Punto 3: Demostró los límites de lo computable.** Con el mismo modelo, Turing demostró que hay problemas que ningún algoritmo puede resolver (el famoso "Problema de la Parada"): no puedes escribir un programa que determine si cualquier programa arbitrario terminará de ejecutarse o se quedará en un bucle infinito para siempre.

### El Test de Turing

En 1950, Turing propuso el siguiente experimento: un humano conversa por texto con una entidad desconocida. Si no puede distinguir si es un humano o una máquina, la máquina supera el test. Es la primera definición operacional de "inteligencia artificial".

---

## John von Neumann y la Arquitectura (1945)

### El problema que existía antes

Los primeros ordenadores electrónicos (como el ENIAC) eran máquinas de propósito específico o semi-específico. Para cambiar el programa que ejecutaban, había que **reconfigurar físicamente el cableado**: desconectar y reconectar cientos de cables durante horas o días. El "programa" no era software, era hardware.

### La idea revolucionaria

En 1945, John von Neumann (matemático húngaro-estadounidense) publicó un informe describiendo una arquitectura diferente: el **programa almacenado**.

La idea clave: **los datos y el programa se almacenan en la misma memoria, en el mismo formato** (como números binarios). La CPU lee instrucciones de la memoria exactamente igual que lee datos.

Esto significa que cambiar el programa es tan sencillo como cargar números distintos en la memoria. No hay que tocar hardware.

### La Arquitectura de Von Neumann

```
┌─────────────────────────────────────────────┐
│ CPU │
│ ┌──────────────┐ ┌──────────────────┐ │
│ │ Unidad de │ │ ALU │ │
│ │ Control │◄──►│ (cálculos y │ │
│ │ │ │ comparaciones) │ │
│ └──────┬───────┘ └──────────────────┘ │
│ │ │
└─────────┼──────────────────────────────────-┘
 │ Bus (canal de datos y direcciones)
 │
┌─────────▼────────────┐ ┌────────────────┐
│ Memoria │ │ Entrada/Salida │
│ (programa + datos │ │ (teclado, │
│ en la misma RAM) │ │ pantalla, │
└──────────────────────┘ │ disco...) │
 └────────────────┘
```

**Los cuatro componentes:**

1. **CPU** (Unidad Central de Procesamiento): contiene la Unidad de Control (que lee y coordina instrucciones) y la ALU (que hace los cálculos).

2. **Memoria**: almacena tanto los datos como el programa. Es donde reside el estado de todo lo que se ejecuta.

3. **Entrada**: teclado, ratón, sensores, disco al leer...

4. **Salida**: pantalla, altavoces, disco al escribir, impresora...

### ¿Por qué sigue siendo relevante?

Prácticamente todos los ordenadores modernos, desde tu teléfono hasta los superordenadores, siguen esta arquitectura en sus fundamentos. Las variaciones modernas (como las cachés, el pipeline o la ejecución fuera de orden) son optimizaciones sobre esta base, no alternativas a ella.

---

## El ENIAC (1945): el primer ordenador de propósito general

### ¿Qué era?

El ENIAC (Electronic Numerical Integrator and Computer) fue construido en la Universidad de Pennsylvania entre 1943 y 1945, financiado por el ejército de Estados Unidos. Su objetivo original: calcular tablas de trayectorias de artillería para la Segunda Guerra Mundial (aunque terminó tarde para eso).

### Características técnicas

|Característica|Datos|
|---|---|
|Peso|27 toneladas|
|Dimensiones|2,4 m de alto × 0,9 m de ancho × 30 m de largo|
|Válvulas de vacío|~18.000|
|Consumo eléctrico|~150 kW (se dice que al encenderlo bajaba la tensión del barrio)|
|Velocidad|5.000 sumas por segundo|
|Fiabilidad|Una válvula se fundía cada dos días aproximadamente|

**El funcionamiento de las válvulas (La "olla hirviendo")** Estas 18.000 válvulas eran, esencialmente, el "abuelo" del transistor. Funcionaban como una bombilla antigua modificada: el filamento interno se calentaba tanto que los electrones empezaban a "hervir" y saltar del metal, como el vapor sale de una **olla hirviendo**.

![a basic vacuum tube diagram, generada por IA](https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcS1T0zQzwyzIbkhwJIac331Gg6j471vv6uMsbYQZA9-j2QlrwcEQxhV4vaWUmV7n2CR89FD52aJu1IpYlEAS1tgkJihpkqIfzlZVKmdTtmAyVtGcow)

Al colocar una placa metálica al otro lado, se creaba un puente de electricidad por el vacío. El secreto estaba en una "rejilla" intermedia que actuaba como una **persiana**: si se le aplicaba carga, bloqueaba el paso de los electrones (**0 binario**); si se quitaba, el flujo pasaba libremente (**1 binario**). Así, el ENIAC usaba el calor y la luz para tomar decisiones lógicas.

Para comparar: un smartphone moderno de gama media realiza miles de millones de operaciones por segundo y cabe en tu bolsillo.

### ¿Cómo se programaba?

No había teclado ni monitor. Programar el ENIAC significaba **reconectar físicamente miles de cables** usando paneles de conexiones similares a las antiguas centralitas telefónicas. Podía llevar días configurarlo para un nuevo problema.

Las seis programadoras principales del ENIAC fueron mujeres matemáticas: Jean Jennings Bartik, Frances Bilas Spence, Kay McNulty Mauchly Antonelli, Marlyn Wescoff Meltzer, Frances Snyder Holberton y Ruth Lichterman Teitelbaum. Fueron contratadas inicialmente como "ordenadores humanas" (su trabajo era calcular tablas manualmente) y terminaron siendo las primeras programadoras de un ordenador electrónico de propósito general. Durante décadas su contribución fue prácticamente ignorada.

### El problema del mantenimiento y los Bugs

 Mantener el ENIAC era una pesadilla. Debido al principio de la "olla hirviendo", el metal de las válvulas terminaba quemándose y rompiéndose constantemente, igual que se funden las bombillas de casa. Además, el calor infernal y el brillo de las 18.000 válvulas atraían a polillas y otros insectos. Estos animales se colaban entre los cables, provocando cortocircuitos al electrocutarse. De ahí nació el término **"Bug" (Bicho)** y la tarea de **"Debugging" (Desbichar)**: los técnicos tenían que abrir la máquina y retirar físicamente los restos de los insectos para que el ordenador volviera a calcular correctamente.

### Las Tarjetas Perforadas

Antes de los teclados, los datos se introducían en los ordenadores mediante **tarjetas perforadas**: cartulinas rígidas rectangulares con un patrón de agujeros.

**¿Cómo funcionaban?**

1. El programador usaba una máquina perforadora (parecida a una máquina de escribir) para perforar agujeros en posiciones específicas de la tarjeta.

2. Un agujero en una posición = 1 (la corriente del lector pasa a través).

3. Ningún agujero = 0 (el cartón bloquea la corriente).

4. La tarjeta se introducía en el lector de la ordenador, que pasaba un peine de contactos eléctricos por encima.

**El gran problema:** tu programa era literalmente una pila física de tarjetas. Si se caían al suelo y se desordenaban, o si alguien las grapaba por error, el programa quedaba inutilizable. Los programadores marcaban una línea diagonal en el canto de las pilas para poder reordenarlas si se revolvían.

Una tarjeta perforada típica de 80 columnas almacenaba 80 caracteres, es decir, 80 bytes. Para meter un programa en un ordenador de los años 50, necesitabas una caja llena de estas tarjetas.

---

## Conexión entre los tres

```
Turing (1936): demuestra que una máquina universal puede resolver cualquier problema computable
 ↓
Von Neumann (1945): diseña la arquitectura para construir esa máquina en hardware real
 ↓
ENIAC y sucesores: primeras implementaciones físicas de esas ideas teóricas
```

---

## Siguiente paso

[[📄08 - Generaciones de la Informática]] → cómo evolucionó el hardware desde las válvulas de vacío hasta la IA y la computación cuántica.