[Amazon EC2 instance type naming conventions - Amazon EC2](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html)

**Tags:** #aws #ec2 #instancias #nomenclatura #cloud-practitioner #cp-computacion

> [!summary] El Código Secreto
> Cuando ves algo como `c6g.xlarge`, no es un nombre aleatorio. Es una fórmula exacta que te dice todo lo que hay dentro de ese servidor físico.

---

## 🔍 Diseccionando el nombre: `c6g.xlarge`

La estructura oficial es: **Familia + Generación + Opciones Adicionales. Tamaño**

1. **`c` (Familia):** Indica para qué está optimizada la máquina. En este caso, la 'c' viene de *Compute* (Computación). 

2. **`6` (Generación):** AWS actualiza sus servidores constantemente. Un número más alto significa hardware más nuevo, moderno y normalmente más barato por el mismo rendimiento. (La generación 6 es más nueva que la 5).

3. **`g` (Opciones Adicionales):** Son letras minúsculas que indican "extras" físicos del hardware. 

	* `g` = Procesadores **G**raviton (hechos por Amazon).

	* `a` = Procesadores **A**MD.

	* `d` = Disco duro local (Instance store) directamente conectado a la placa base.
	
4. **`xlarge` (Tamaño):** Indica la "talla" de la camiseta. A mayor talla, más CPUs y más RAM (y más cara es la hora).

	* Tallas típicas: `nano`, `micro`, `small`, `medium`, `large`, `xlarge`, `2xlarge`, `4xlarge`... `24xlarge`.

* ![[🏷️ Nomenclatura EC2. Cómo leer el nombre de una Instancia-1.png]]

> [!important] Regla de Oro del Precio
> Dentro de la misma familia y generación, si pasas de `large` a `xlarge` (doblas el tamaño), **el precio se multiplica exactamente por dos**. Escalar es un cálculo matemático perfecto.

---

---
→ Volver al índice: [[📂Computacion/00 - Índice Computacion|🪐 Computacion]]
