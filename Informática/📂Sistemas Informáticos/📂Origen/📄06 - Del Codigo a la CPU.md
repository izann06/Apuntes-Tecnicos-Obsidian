
> El camino que recorre tu código desde el editor hasta los transistores de la CPU.

---

## Las capas de abstracción

La informática funciona por capas. Cada capa oculta la complejidad de la capa inferior y ofrece herramientas más fáciles de usar a la capa superior. Este concepto se llama **abstracción**.

```
Tu código (Python, Java, C#) ← tú trabajas aquí
 ↓ compilador / intérprete
Código intermedio o ensamblador
 ↓ ensamblador (assembler)
Código máquina (binario puro) ← la CPU trabaja aquí
 ↓
Transistores abriendo y cerrando
```

---

## Nivel 1: Código de alto nivel

Es el código que escribes en el IDE (VS Code, IntelliJ, PyCharm...). Está diseñado para ser legible por humanos:

```java
int suma = 2 + 2;
System.out.println(suma);
```

La CPU no puede ejecutar esto directamente. Necesita instrucciones muy específicas y en formato binario.

---

## Nivel 2: El Compilador (o el Intérprete)

El compilador es un programa que lee tu código de alto nivel y lo traduce a algo que la máquina puede ejecutar. Hay dos enfoques principales:

### Compilación (C, C++, Go, Rust)

El código se traduce **antes de ejecutarse**, generando un archivo ejecutable. El proceso:

1. **Análisis léxico**: el compilador lee el código carácter a carácter e identifica tokens (`int`, `suma`, `=`, `2`, `+`, `2`, `;`).

2. **Análisis sintáctico**: verifica que la gramática es correcta (que el código tiene sentido según las reglas del lenguaje).

3. **Análisis semántico**: comprueba el significado (¿tiene sentido sumar un entero con una cadena de texto?).

4. **Generación de código intermedio**: muchos compiladores producen primero código en ensamblador como paso intermedio (permite optimizar y ver qué está haciendo el compilador).

5. **Optimización**: el compilador reorganiza y mejora el código para que sea más rápido.

6. **Generación de código máquina**: el ensamblador convierte el código ensamblador en binario puro.

El resultado es un archivo `.exe` (Windows) o sin extensión (Linux/Mac) que contiene instrucciones en binario listas para la CPU.

### Interpretación (Python, JavaScript básico, Ruby)

El código no se compila por completo antes de ejecutarse. Un programa llamado **intérprete** lee el código línea a línea y lo ejecuta en tiempo real.

- Ventaja: más flexible y fácil de depurar.

- Desventaja: más lento (tiene que traducir en tiempo de ejecución).

### Compilación a bytecode (Java, C#, Kotlin)

Java usa un enfoque híbrido:

1. El compilador de Java traduce tu código a **bytecode** (un formato intermedio, no binario nativo).

2. La **JVM** (Java Virtual Machine) interpreta o compila ese bytecode al vuelo (JIT, Just-In-Time compilation) para la CPU específica donde se ejecuta.

Esto es lo que hace que Java sea "write once, run anywhere": el bytecode es el mismo en Windows, Linux y Mac; la JVM se encarga de adaptarlo a cada procesador.

---

## Nivel 3: Ensamblador (Assembly)

El ensamblador es un lenguaje de muy bajo nivel donde cada instrucción corresponde directamente a una instrucción de la CPU. No tiene bucles `for` ni funciones complejas. Solo operaciones elementales:

```asm
MOV AX, 2 ; mueve el valor 2 al registro AX
ADD AX, 2 ; suma 2 al registro AX (AX ahora contiene 4)
```

Cada instrucción en ensamblador tiene un equivalente exacto en binario (código máquina). El **ensamblador** (assembler, el programa) hace esa traducción directa.

¿Por qué existe este paso intermedio? Porque los ingenieros necesitan a veces inspeccionar cómo el compilador está optimizando el código, y el ensamblador es legible por humanos (a duras penas, pero legible). También porque algunos programas críticos (sistemas operativos, drivers) se escriben parcialmente en ensamblador para máxima velocidad.

---

## Nivel 4: Código máquina (binario)

Son las instrucciones que la CPU entiende directamente. Cada tipo de procesador tiene su propio **conjunto de instrucciones** (ISA, Instruction Set Architecture):

- **x86 / x86-64**: Intel y AMD. Los procesadores de la mayoría de ordenadores de escritorio y portátiles.

- **ARM**: Apple Silicon (M1, M2...), procesadores de móviles, Raspberry Pi.

- **RISC-V**: arquitectura abierta emergente.

Un binario compilado para x86 no se puede ejecutar directamente en ARM (por eso los juegos de Windows no corren directamente en Mac sin herramientas de traducción como Rosetta 2).

---

## Nivel 5: El Sistema Operativo (SO)

Cuando haces doble clic en un ejecutable:

1. El SO (Windows, Linux, macOS) lee el archivo del disco duro.

2. Copia las instrucciones (en binario) a la **RAM** (memoria de acceso aleatorio).

3. Le dice a la CPU en qué dirección de memoria empiezan las instrucciones.

4. La CPU empieza a leer y ejecutar esas instrucciones, una a una o varias a la vez si hay múltiples núcleos.

El SO también actúa de árbitro: gestiona qué programa usa la CPU en cada momento (multitarea), controla el acceso a la memoria para que un programa no rompa a otro, y gestiona los dispositivos de entrada/salida.

---

## Resumen del viaje completo

```
Tú escribes: int suma = 2 + 2;

Compilador genera: MOV AX, 2
 ADD AX, 2

Ensamblador genera: 10111000 00000010 (MOV AX, 2 en binario x86)
 00000101 00000010 (ADD AX, 2 en binario x86)

SO carga en RAM: [esos bytes en una dirección de memoria]

CPU ejecuta: Lee la instrucción → pasa por ALU → resultado en registro → siguiente instrucción

Transistores: Miles de millones abriéndose y cerrándose en nanosegundos
```

---

## Preguntas
### 1.Intérprete vs. Compilador y el "Truco" de Java

Para entender esto, imagina que has escrito un libro de recetas en español y quieres que un chef francés lo cocine. El chef francés es la CPU (solo entiende código máquina).

- **El Compilador (Ej. C, C++): El Traductor de Libros.** Coges todo tu libro en español, contratas a un traductor, y te devuelve un libro impreso 100% en francés (el archivo `.exe`).
 
 - _Ventaja:_ El chef lo lee rapidísimo y del tirón.
 
 - _Desventaja:_ Si le mandas ese libro a un chef alemán (un procesador ARM o un Mac), no lo entenderá. Tienes que compilar un libro distinto para cada país.
 
- **El Intérprete (Ej. Python, JavaScript básico): El Traductor Simultáneo.** Te vas a Francia con tu libro en español y contratas a un tipo que se pone al lado del chef. Tú le lees una línea en español, él la traduce al francés en voz alta, el chef la hace. Luego la siguiente línea.
 
 - _Ventaja:_ Puedes llevar tu libro en español a cualquier país si contratas a un traductor local (el intérprete de Python está instalado en todos los OS).
 
 - _Desventaja:_ Es más lento. El chef tiene que esperar a que el tipo termine de hablar por cada paso.
 

**El Mix de Java (El Bytecode y la Máquina Virtual)** Java dijo: _"Quiero la velocidad del compilador pero la flexibilidad del intérprete"_. Así que inventaron un paso intermedio.

1. **Paso 1 (Compilador `javac`):** Compila tu código Java... pero NO a código máquina francés ni alemán. Lo compila a un idioma inventado llamado **Esperanto (Bytecode)**. Tu archivo `.java` se convierte en `.class`.
 
2. **Paso 2 (La JVM - Intérprete/JIT):** Cuando instalas Java en Windows, Linux o Mac, instalas la **Máquina Virtual de Java (JVM)**. La JVM es un programa que es experto en leer ese Esperanto (Bytecode) y traducirlo sobre la marcha a las instrucciones exactas que necesita la CPU de ese ordenador.
 

Por eso el lema de Java es _"Escribe una vez, ejecuta en cualquier parte"_. Tú compilas el Bytecode una vez, y la JVM de cada ordenador se encarga del trabajo sucio final.

---

### 2. ¿Puedo "robar" las mejoras del compilador para mi código?

Esta idea es buenísima. Podrías pensar: _"Si el compilador coge mi código torpe y lo hace perfecto, voy a ver cómo lo ha dejado y lo escribo así desde el principio"_.

**La respuesta corta es: No. No puedes, y si pudieras, sería una idea terrible.**

Te explico por qué con el ejemplo clásico de optimización llamado **"Desenrrollado de Bucles" (Loop Unrolling)**:

Tú en Java escribes un código limpio y fácil de leer para un humano:

Java

```
for (int i = 0; i < 3; i++) {
 System.out.println("Hola");
}
```

El compilador mira eso y dice: _"Un bucle requiere que la CPU sume 1 a la variable, compruebe si es menor que 3, y vuelva a saltar arriba. Eso gasta ciclos de reloj. Como solo son 3 veces, voy a destruir el bucle"_.

La optimización que genera el compilador por debajo es el equivalente a esto:

Java

```
System.out.println("Hola");
System.out.println("Hola");
System.out.println("Hola");
```

Es infinitamente más rápido para la CPU ejecutar tres instrucciones seguidas que gestionar un bucle.

**¿Por qué no debes poner eso en tu código?**

1. **Mantenibilidad:** Si el bucle fuera de 10.000 iteraciones, ¿vas a copiar y pegar 10.000 veces la línea? Tu código sería ilegible. El trabajo del programador es escribir código _mantenible para humanos_. El trabajo del compilador es destrozar ese código para hacerlo _rápido para máquinas_.
 
2. **Optimizaciones de Hardware:** Muchas optimizaciones implican mover variables a registros físicos ultra-rápidos de la CPU (como el registro `AX` o `R1`). En lenguajes de alto nivel como Java o Python, ni siquiera tienes "palabras" para nombrar esos registros. Físicamente, no puedes escribir esa mejora en tu editor.
 

---

### 3. ¿Todos pasan por el Ensamblador?

**No. Esto es un error muy común.**

El Ensamblador (`MOV AX, 2`) es un lenguaje de texto diseñado para que los humanos puedan leer las instrucciones de la máquina sin volverse locos leyendo ceros y unos (`10111000...`).

- Los compiladores modernos (como GCC o los basados en LLVM) **no necesitan escupir un archivo de texto en Ensamblador**. Pasan tu código a una representación matemática interna (llamada AST y luego IR - _Intermediate Representation_), aplican las optimizaciones ahí, y directamente escriben el archivo binario (`.exe`) lleno de ceros y unos.
 
- Solo pasan por el formato de texto Ensamblador si el programador le pone una "bandera" especial al compilador diciendo: _"Oye, expórtame un archivo de texto para que yo pueda leer y auditar qué diablos estás haciendo por debajo"_.
 
- Los intérpretes (como Python) ni siquiera se acercan al Ensamblador. Pasan el código a sus propias estructuras de datos en la memoria y van ejecutando pequeñas rutinas pre-programadas en C que ya estaban compiladas.


## Siguiente paso

[[07 - Pioneros]] → antes de que todo esto existiera, hubo mentes que diseñaron la teoría: Turing, Von Neumann y el ENIAC.