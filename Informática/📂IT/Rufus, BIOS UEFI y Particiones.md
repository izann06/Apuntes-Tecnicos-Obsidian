## 1. Rufus y la Creación de Medios de Arranque

### 🧠 Conceptos Fundamentales

Antes de utilizar la herramienta, es vital entender qué estamos manipulando:

- **¿Qué es una imagen `.iso`?**
    
    Es un archivo que contiene una **copia exacta y completa** (un "clon" digital) de un sistema de archivos de un disco óptico (CD/DVD) o de una unidad de almacenamiento. No es solo una carpeta con archivos; mantiene la estructura, el sector de arranque y la jerarquía necesaria para que el software funcione exactamente igual que el medio original.
    
- **¿Qué significa que un USB sea "Booteable" (de arranque)?**
    
    Un USB booteable está configurado a bajo nivel para que, al encender el ordenador, el hardware del equipo (la BIOS/UEFI) pueda leer un "sector de arranque" especial en el pendrive y ejecutar el sistema operativo o la herramienta instalada en él _antes_ de que cargue el Windows que está en el disco duro.
    

> [!WARNING] Cuidado: El Formateo Total
> 
> Al usar Rufus, el pendrive debe ser **formateado completamente**. Esto significa que Rufus borrará la tabla de particiones actual y creará una nueva. **Se perderán todos los datos del USB de forma irreversible.** Es absolutamente obligatorio hacer una copia de seguridad de lo que haya en el pendrive antes de empezar.

### 🛠️ ¿Qué es Rufus y para qué sirve?

**Rufus** es un programa para Windows, gratuito, de código abierto y muy ligero. Es la herramienta estándar en el sector IT para manipular unidades de almacenamiento extraíbles (pendrives, tarjetas SD). Sirve principalmente para:

- **Instalar o reinstalar** sistemas operativos (Windows, Linux, etc.).
    
- **Ejecutar herramientas de rescate** o reparación a bajo nivel (cuando el sistema principal no arranca).
    
- **Actualizar el firmware** (BIOS/UEFI) de una placa base desde DOS.
    

### ⚙️ ¿Cómo se hace? (Procedimiento Técnico)

1. **Descargar la ISO:** Consigue el archivo `.iso` del sistema operativo (ej. Windows 11 o Ubuntu).
    
2. **Conexión y Selección:** Inserta el pendrive y selecciónalo en el apartado _Dispositivo_ de Rufus. (Recuerda la advertencia del formateo).
    
3. **Carga de la ISO:** En _Elección de arranque_, selecciona tu archivo `.iso`.
    
4. **Configuración de Esquema (Punto Clave):**
    
    - PC antiguo (BIOS) ➡️ Elige **MBR**.
        
    - PC moderno (UEFI) ➡️ Elige **GPT**.
        
5. **Empezar:** Haz clic en "Empezar" y espera a que termine el proceso de escritura.
    

---

## 2. El Firmware: BIOS vs. UEFI

El firmware es el primer código que se ejecuta al encender el ordenador. Su trabajo es **inicializar el hardware** (comprobar que la RAM, el procesador y los discos funcionan) y luego "pasar el relevo" (hacer _boot_) al sistema operativo.

### 🟦 BIOS (Basic Input/Output System)

- **Época:** La tecnología antigua (nació en los años 80).
    
- **Arquitectura:** Sistema de 16 bits.
    
- **Límites:** Solo maneja discos duros de hasta **2.2 TB** y es bastante lento iniciando el hardware.
    
- **Interfaz:** Suele ser la clásica pantalla azul o negra, navegable únicamente con las flechas del teclado.
    
- **Compatibilidad:** Utiliza el esquema de particiones **MBR**.
    

### 🟩 UEFI (Unified Extensible Firmware Interface)

- **Época:** El estándar moderno. Reemplazó a la BIOS (es el "nuevo motor" debajo del capó).
    
- **Arquitectura:** Trabaja a 32 o 64 bits.
    
- **Ventajas:** Maneja discos de tamaños colosales (Zettabytes), inicia el sistema operativo rapidísimo y cuenta con funciones de seguridad avanzadas como el **Secure Boot** (Arranque Seguro).
    
- **Interfaz:** Puede soportar gráficos avanzados y uso del ratón, pero no es obligatorio.
    
- **Compatibilidad:** Utiliza el esquema de particiones **GPT**.
    

> [!INFO] ¿Por qué le seguimos llamando BIOS si tenemos UEFI?
> 
> 1. **El peso de la costumbre:** Al igual que llamamos "Kleenex" a cualquier pañuelo, los técnicos dicen "voy a entrar a la BIOS" por pura inercia, aunque el PC sea de última generación.
>     
> 2. **No todo es visual:** UEFI es un código reescrito desde cero. Muchos equipos de oficina modernos usan UEFI por dentro, pero mantienen una interfaz visual de texto (sin ratón) por simplicidad. Parecen BIOS, pero son UEFI.
>     
> 3. **Modo Legacy (CSM):** Los sistemas UEFI incluyen un "Modo de compatibilidad heredada". Esto permite que una placa moderna "se disfrace" de BIOS antigua para poder instalar sistemas operativos muy viejos que no entienden cómo hablar con UEFI.
>     

---

## 3. Tablas de Particiones: MBR vs. GPT

Para que Rufus sepa cómo preparar el USB, y el firmware sepa cómo leer el disco duro, se necesita un "índice" que diga cómo están organizados los datos. Eso es la tabla de particiones.

### 🗄️ MBR (Master Boot Record)

- **Diseño:** Creado para la **BIOS** antigua.
    
- **Límites de tamaño:** No puede manejar discos de más de **2 TB** (si conectas un disco de 4 TB, solo verá la mitad).
    
- **Límites de partición:** Solo permite crear **4 particiones primarias**.
    
- **Seguridad:** Guarda toda la información de arranque en un solo sector al principio del disco. Si ese sector se daña (o un virus lo ataca), el sistema operativo no arrancará.
    

### 🗂️ GPT (GUID Partition Table)

- **Diseño:** Creado para funcionar de la mano con **UEFI**.
    
- **Límites de tamaño:** Prácticamente ilimitado (hasta 9.4 Zettabytes).
    
- **Límites de partición:** Hasta **128 particiones primarias** (en Windows).
    
- **Seguridad:** Redundante y seguro. Guarda múltiples copias de los datos de arranque distribuidas por todo el disco. Si la cabecera principal se daña, GPT puede recuperar los datos de una copia de seguridad interna automáticamente.
    

---

## 4. Guía de Acceso a la BIOS/UEFI

Para configurar desde dónde arranca el PC (por ejemplo, para que lea tu USB de Rufus en lugar del disco duro), debes acceder al menú de configuración del firmware presionando una tecla específica justo en el momento de encender el ordenador.

No hay un estándar universal, depende del fabricante:

| **Marca / Fabricante**           | **Tecla(s) de Acceso a BIOS/UEFI** | **Notas Adicionales**                                                                                                                |
| -------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **General / Universal**          | `F2` o `Supr` (`Del`)              | Las combinaciones más comunes en placas de sobremesa.                                                                                |
| **HP**                           | `F10`                              | A veces requiere presionar `Esc` primero para abrir un menú.                                                                         |
| **Dell**                         | `F2`                               |                                                                                                                                      |
| **Lenovo**                       | `F2` o `Fn` + `F2`                 | Algunos portátiles tienen un **"Botón Novo"** físico lateral (diminuto, se pulsa con un clip con el PC apagado para entrar directo). |
| **Asus / Acer / Gigabyte / MSI** | `Supr` (`Del`) o `F2`              |                                                                                                                                      |

> [!HINT] Boot Menu (Menú de arranque rápido)
> 
> Si solo quieres elegir el USB de forma puntual sin entrar a configurar toda la BIOS/UEFI completa, muchos PCs tienen una tecla dedicada para el **Boot Menu**. Suele ser `F12`, `F8` o `F11`.