
> La CPU solo entiende corriente o no corriente. Todo lo demás (letras, fotos, vídeos) es una capa de convención construida sobre esa base física.

---
## ¿Por qué binario y no decimal?

Pregunta muy natural: los humanos usamos el sistema decimal (0-9) porque tenemos diez dedos. ¿Por qué los ordenadores usan binario?

La respuesta es física. Un transistor tiene dos estados estables y fiables: conduce (1) o no conduce (0). Si quisiéramos que un transistor representara 10 valores distintos (del 0 al 9 como en decimal), tendría que distinguir entre 10 niveles de voltaje diferentes. Eso es extremadamente propenso a errores: una pequeña interferencia o variación de temperatura haría que el 4 se confundiera con el 5. Con dos estados bien diferenciados (corriente/sin corriente), el sistema es robusto y fiable.

---
## El sistema binario

El sistema binario es base 2: solo usa dos dígitos, 0 y 1. Funciona igual que el sistema decimal, pero con potencias de 2 en lugar de potencias de 10.

### Conversión de binario a decimal

En decimal, el número 342 significa:

- 3 × 10² + 4 × 10¹ + 2 × 10⁰ = 300 + 40 + 2 = 342

En binario, el número `1011` significa:

- 1 × 2³ + 0 × 2² + 1 × 2¹ + 1 × 2⁰ = 8 + 0 + 2 + 1 = **11 en decimal**

---

## Bit y Byte

### Bit

Un bit (binary digit) es la unidad mínima de información: un solo 0 o un solo 1. Un transistor almacena un bit.

### Byte: ¿por qué 8 bits?

Un byte son 8 bits. ¿Por qué 8 y no 10 o 16?

La razón es histórica y práctica. IBM estandarizó el byte de 8 bits en los años 60 porque:

1. 8 bits permiten 256 combinaciones, suficientes para representar todos los caracteres de texto necesarios en inglés.

2. 8 es potencia de 2 (2³), lo que hace que las operaciones en circuitos lógicos sean elegantes y eficientes.

3. Se puede dividir fácilmente en dos grupos de 4 bits (nibbles), útil para representar dígitos hexadecimales.

### ¿Por qué de 0 a 255?

Con 8 bits, cada uno puede ser 0 o 1. El número total de combinaciones posibles es:

```
2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 2⁸ = 256 combinaciones
```

Si empezamos a contar desde 0, llegamos hasta el 255. El mínimo (00000000) es 0 y el máximo (11111111) es:

```
128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255
```

---

## ASCII: el diccionario de letras

La CPU solo sabe sumar números. No tiene ni idea de qué es una "A" o una "z". Para solucionar esto, en 1963 se creó el estándar ASCII (American Standard Code for Information Interchange): un diccionario que asigna un número a cada carácter.

### Ejemplos ASCII

| Carácter | Número decimal | Binario (8 bits) |
| ---------- | -------------- | ---------------- |
| A | 65 | 01000001 |
| B | 66 | 01000010 |
| Z | 90 | 01011010 |
| a | 97 | 01100001 |
| 0 (dígito) | 48 | 00110000 |
| Espacio | 32 | 00100000 |
| ! | 33 | 00100001 |
| | | |

Cuando pulsas la tecla "A" en tu teclado, el hardware envía el número 65 al sistema. Ese número 65 se almacena en memoria como `01000001`. Cuando el programa quiere mostrarlo en pantalla, consulta el diccionario y dibuja el glifo de la "A".

### Limitaciones del ASCII

Era un diccionario muy pequeño. Cada letra ocupaba siempre **1 Byte (8 bits)**. Esto daba un máximo de 256 combinaciones. Servía para el inglés, pero no cabían las tildes, las 'ñ', el chino o el árabe.

**La revolución del UTF-8 (El diccionario elástico):** En los años 90 se inventó UTF-8, un estándar que permite codificar todos los lenguajes del mundo y emojis. Su genialidad es que es **de tamaño variable**: el programa gasta más o menos transistores (Bytes) dependiendo de lo rara que sea la letra.

- **1 Byte:** Letras básicas y números (A, B, C, 1, 2).
 
- **2 Bytes:** Letras con tildes, la ñ, símbolos europeos (á, é, ñ).
 
- **3 Bytes:** Símbolos asiáticos (Chino, Japonés).
 
- **4 Bytes:** Emojis y símbolos muy antiguos (🚀, 😂). Un emoji gasta cuatro veces más memoria RAM que una letra normal.
 

**El "Tragamiento" (Retrocompatibilidad):** ¿Por qué UTF-8 triunfó sin romper los ordenadores antiguos? Porque **UTF-8 se "tragó" al ASCII**. Los creadores hicieron que los primeros 128 caracteres de UTF-8 tuvieran exactamente el mismo código binario que el ASCII antiguo.

- La "A" en ASCII antiguo: `01000001`
 
- La "A" en UTF-8 moderno: `01000001` Gracias a esto, un programa viejo puede leer un texto moderno sin enterarse de que el diccionario ha cambiado. Hoy en día, UTF-8 es el estándar universal en internet y en la programación.

> [!NOTE] UTF-32: El enfoque de "Fuerza Bruta"
> 
> Imagínate que estás diseñando el diccionario y dices: _"Mira, estoy harto de letras elásticas. Vamos a hacer que **TODAS** las letras ocupen 4 Bytes fijos"_.
> 
> - **Ventaja (Velocidad para la CPU):** Es rapidísimo para buscar. Si el ordenador quiere saltar a la letra número 1.000 de un texto, solo tiene que multiplicar $1000 \times 4$ y saltar a ese byte exacto de la memoria. Con UTF-8, la CPU tiene que leer el texto desde el principio, letra por letra, para saber cuánto mide cada una.
> 
>
> - **Desventaja (Pesadilla de Memoria):** Es un derroche absoluto. Si escribes un simple "Hola" (4 letras básicas), en UTF-8 gastas 4 Bytes. En UTF-32 gastas **16 Bytes**. Se llena el disco duro de ceros inútiles. Casi nadie lo usa para guardar archivos.
> 

---

> [!ABSTRACT] UTF-16: El punto medio (Java/Windows)
> 
> En UTF-16, el tamaño mínimo es de **2 Bytes**. Intenta equilibrar el ahorro de espacio con la facilidad de procesamiento.
> 
> |**Carácter**|**Espacio**|
> |---|---|
> |Inglés / Tildes|2 Bytes|
> |Símbolos Asiáticos|2 Bytes (¡Aquí ahorra más que UTF-8!)|
> |Emojis (🚀)|4 Bytes|
> 
> **¿Por qué se usa?** Por historia. En los 90, Java y Windows creyeron que 65,536 combinaciones (2 bytes) serían suficientes para siempre. Cuando llegaron los emojis, tuvieron que meter un "parche" para usar 4 bytes.

---

> [!Warning] La Batalla: Red vs. RAM
> 
> - **UTF-8 (Internet/Disco):** Es el rey absoluto porque la mayoría del texto web es inglés/código, y UTF-8 es el más ligero para enviar por cables.
> 
> - **UTF-16 (Memoria RAM):** Java y Windows lo mantienen en RAM porque procesar matemáticamente bloques de 2 bytes es más eficiente que el sistema elástico de UTF-8.
>

![[📄05 - Código Binario y ASCII.png]]

---

## ¿Cómo se representa todo lo demás?

Todo lo que existe en un ordenador es una secuencia de bits interpretada de una forma u otra:

| Tipo de dato | Cómo se representa |
| -------------- | ---------------------------------------------------------------- |
| Texto | Números según tabla ASCII/Unicode |
| Número entero | Binario directo (con bit de signo para negativos) |
| Número decimal | Estándar IEEE 754 (coma flotante) |
| Color (píxel) | 3 bytes: uno para rojo, uno para verde, uno para azul (RGB) |
| Imagen | Millones de píxeles, cada uno con sus 3 bytes de color |
| Audio | Muestras de amplitud de onda grabadas miles de veces por segundo |
| Vídeo | Secuencia de imágenes comprimidas + audio |
| Programa | Instrucciones codificadas como números que la CPU interpreta |

No existe ninguna magia en ningún nivel. Todo son números. La diferencia entre una foto y un programa es cómo el sistema interpreta esos números.

---

## Unidades de almacenamiento

| Unidad | Equivalencia | Ejemplo |
| --------------- | ------------ | ---------------------------------- |
| 1 Bit | 0 o 1 | Un transistor |
| 1 Byte | 8 bits | Un carácter de texto |
| 1 Kilobyte (KB) | 1.024 bytes | Un texto corto |
| 1 Megabyte (MB) | 1.024 KB | Una foto sin comprimir |
| 1 Gigabyte (GB) | 1.024 MB | Una película HD |
| 1 Terabyte (TB) | 1.024 GB | Disco duro típico |
| 1 Petabyte (PB) | 1.024 TB | Datos de un centro de datos grande |

### Te preguntarás por qué son 1024 siempre y no 1000

La respuesta es que como vimos antes la informática funciona en Base 2 (Binario) y no Base 10 (Decimal).En decimal si estaría bien pero en Binario no porque va de la siguiente manera.

2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048...

En los años 60, los informáticos vieron que 1024 estaba muy cerca de 1000, así que tomaron prestada la palabra humana "Kilo" y crearon el **Kilobyte (1 KB = 1024 Bytes)**.

**¿Y Qué pasa cuando compras un disco duro de 1 TB, porque luego nunca tiene 1TB de espacio?** 

1. **El Fabricante (Usa Base 10 para vender más):** Te vende 1.000.000.000.000 de bytes físicos. Como divide entre 1.000, para él eso es exactamente **1 Terabyte (1 TB)**.
 
2. **Windows (Usa Base 2 para trabajar):** Coge ese mismo billón de bytes, pero los agrupa dividiendo entre 1024. Al usar "cajas" más grandes, el número final baja a **931 GB**.

	- Tiene 1.000.000.000.000 bytes.
	 
	- Lo divide entre 1024 = 976.562.500 Kilobytes (KB).
	 
	- Lo divide entre 1024 = 953.674 Megabytes (MB).
	 
	- Lo divide entre 1024 = **931,32 Gigabytes (GB)**.

---

## Siguiente paso

[[06 - Del Código a la CPU]] → ahora que sabemos cómo el hardware representa datos, veamos cómo tu código Python o Java llega a convertirse en esos bits que la CPU ejecuta.