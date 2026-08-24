
> Un transistor solo sabe abrir o cerrar. Cuando conectas varios entre sí, aparece la lógica.

---

## ¿Qué es una puerta lógica?

Una puerta lógica es un **circuito formado por transistores conectados entre sí** que toma una o varias entradas (0s y 1s) y produce una salida según una regla matemática fija.

El transistor por sí solo solo puede decir "sí pasa" o "no pasa". La puerta lógica convierte esa capacidad básica en **decisiones**: ¿pasa corriente si las dos entradas están activas? ¿O si solo una lo está? ¿O si ninguna?

---

## Las puertas lógicas


![[📄04 - Puertas Lógicas y ALU-1.png]]
![[📄04 - Puertas Lógicas y ALU-2.png]]
![[📄04 - Puertas Lógicas y ALU-3.png]]
## ¿Sin puertas lógicas qué pasaría?

Solo tendríamos transistores individuales que pueden encenderse y apagarse, pero sin ninguna capacidad de procesar información. No podríamos sumar, comparar, seleccionar. La computación tal como la conocemos no existiría. Las puertas lógicas son el primer nivel donde el hardware empieza a hacer algo con los datos.

---

## La ALU: Unidad Aritmético Lógica

La ALU (Arithmetic Logic Unit) es el componente de la CPU donde ocurren todos los cálculos. Es, literalmente, un bloque masivo de puertas lógicas cuidadosamente diseñadas para realizar operaciones específicas.

### ¿Qué operaciones hace la ALU?

**Aritméticas:**

- Suma (ADD)
- Resta (SUB)
- Multiplicación (en CPUs modernas, hay unidades dedicadas)
- División

**Lógicas (bit a bit):**

- AND, OR, NOT, XOR entre dos números
- Desplazamientos de bits (shift left / shift right, equivalente a multiplicar o dividir por 2)

**Comparaciones:**

- ¿A es igual a B?
- ¿A es mayor que B?
- ¿A es cero?

### ¿Cómo suma la ALU?

El componente básico es el **sumador de 1 bit** (Full Adder), construido con puertas XOR, AND y OR. Toma dos bits de entrada más un acarreo (carry) y produce un bit de resultado y un acarreo de salida.

Encadenando 64 de estos sumadores de 1 bit obtienes un sumador de 64 bits, que es lo que usa una CPU moderna para sumar dos números de 64 bits.

### La ALU dentro de la CPU

```
CPU
├── Unidad de Control (CU) → lee las instrucciones y coordina todo
├── ALU → hace los cálculos
├── Registros → memoria ultrarrápida interna (guarda los datos temporales)
└── Caché → memoria rápida entre la RAM y los registros
```

La Unidad de Control le dice a la ALU qué operación hacer y con qué datos. La ALU los procesa y devuelve el resultado.

---

## Resumen visual de la cadena

```
Transistores → Puertas lógicas → Sumadores y comparadores → ALU → CPU
(física)        (lógica básica)   (operaciones compuestas)   (cálculo) (procesamiento)
```

---

## Siguiente paso

[[05 - Código Binario y ASCII]] → ahora que entendemos el hardware, veamos cómo representa datos: números, letras, imágenes.