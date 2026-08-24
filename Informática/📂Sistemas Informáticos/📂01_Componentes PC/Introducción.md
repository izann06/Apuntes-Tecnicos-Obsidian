## 🔹 CPU (Procesador)

- **Función principal**: Ejecuta instrucciones y cálculos que le envían los programas. Es el cerebro de la computadora.
    
- **Ejemplo de uso**: Cuando abres un Word, la CPU interpreta cada acción que haces: abrir archivo, escribir, guardar, copiar, pegar.
    
- ### Núcleo (Core)

- Un núcleo es como un “mini cerebro” dentro del CPU.
    
- Cada núcleo **puede ejecutar instrucciones de forma independiente**.
    
- Ejemplo: si tienes un CPU de 4 núcleos, es como tener 4 trabajadores independientes que pueden hacer cosas al mismo tiempo.
    

###  Hilo (Thread)

- Un hilo es una **línea de ejecución de instrucciones**. Es la tarea que un núcleo puede manejar.
    
- Algunos CPUs tienen **Hyper-Threading o SMT**, lo que permite que **cada núcleo maneje 2 hilos al mismo tiempo**.
    
- Ejemplo: un núcleo con Hyper-Threading puede manejar 2 hilos → el CPU de 4 núcleos tiene 8 hilos.
    

###  ¿Qué significa que pueda ejecutar 8 tareas simultáneamente?

- No significa que solo puedas abrir 8 programas.
    
- **Tarea ≠ programa**. Una tarea es una “instrucción en ejecución”.
    
    - Un solo programa puede generar **muchas tareas o hilos**.
        
    - Ejemplo: Chrome abierto con 20 pestañas = cientos de hilos, algunos para cada pestaña, otros para procesos internos.
        
- El CPU **intercala** los hilos muy rápido, dando la sensación de que todo se ejecuta al mismo tiempo.
    

### ¿Están los hilos separados o conectados?

- Los hilos de un mismo núcleo **comparten recursos internos** del núcleo (caché, ALU parcialmente).
    
- Los núcleos son más independientes entre sí, pero todos están conectados al **bus del CPU** para acceder a RAM y otros componentes.
    
- Por eso, más núcleos = mejor multitarea real; más hilos por núcleo = más eficiencia, pero menos “independencia completa”.
    

### Ejemplo práctico

Supón que tienes:

- CPU de 4 núcleos y 8 hilos (con Hyper-Threading).
    

Entonces:

1. Cada núcleo puede ejecutar **2 hilos**.
    
2. Puedes abrir un navegador, Word, Photoshop y un juego. Cada programa puede tener **varios hilos**, y el CPU va asignando cada hilo a un núcleo disponible.
    
3. El sistema operativo hace **planificación (scheduling)** para que todos los hilos reciban tiempo de CPU, y se nota todo fluido.
    



💡 **Resumen sencillo**:

- Núcleo = trabajador físico.
    
- Hilo = tarea que ese trabajador puede manejar.
    
- 2 hilos por núcleo ≈ 2 tareas “virtuales” que se ejecutan casi al mismo tiempo en un núcleo.
    
- Muchísimos programas y procesos = muchos hilos, el CPU los intercala super rápido.
    



## 🔹 Memoria

### 1. RAM (Memoria de acceso aleatorio)

- **Función**: Almacena datos que los programas necesitan mientras se están ejecutando.
    
- **Ejemplo**: Si abres Photoshop y un archivo grande de imagen, la RAM guarda los datos de esa imagen para que puedas editarla rápidamente.
    
- **Por qué a veces no se borran las pestañas del navegador**:
    
    - Muchos navegadores guardan las **pestañas en disco** usando caché o archivos de sesión antes de apagar.
        
    - La RAM sí se borra, pero la información importante se copia al **SSD/HDD** temporalmente.
        

### 2. ROM

- Contiene instrucciones permanentes, como el **BIOS/UEFI** que inicia el hardware al encender la PC.
    
- **Ejemplo**: Sin ROM, la computadora no sabría cómo encenderse ni encontrar el sistema operativo.
    

### 3. Discos

- **HDD**: disco duro magnético.
    
    - **Ejemplo**: Guardar películas, música o documentos grandes.
        
    - Pros: barato y mucha capacidad. Contras: más lento, ruidoso.
        
- **SSD SATA**: almacenamiento sólido, más rápido.
    
    - **Ejemplo**: Sistema operativo y programas se cargan en segundos.
        
- **NVMe / M.2**: ultra rápido conectado al bus PCIe.
    
    - **Ejemplo**: Juegos pesados, edición de video 4K, IA.
        
    - La velocidad se mide en GB/s, comparado con los MB/s de HDD.
        



## 🔹 Tarjeta gráfica (GPU)

- **Función**: Procesa gráficos, video, y tareas de cálculo paralelo.
    
- **Ejemplo de uso**:
    
    - Juegos 3D: calcula la posición, luz y textura de cada objeto.
        
    - Edición de video: renderiza efectos en tiempo real.
        
    - IA / Machine Learning: realiza miles de cálculos simultáneos.
        
- **Tipos**:
    
    - **Integrada**: dentro del CPU, menos potente.
        
    - **Dedicada**: separada, con memoria VRAM propia.
        
- **Otros componentes**:
    
    - Núcleos CUDA (NVIDIA) o Stream Processors (AMD): para cálculos paralelos.
        
    - VRAM: memoria rápida de la GPU para texturas y datos gráficos.
        



## 🔹 Fuente de alimentación (PSU)

- **Función**: Convierte la corriente de la pared (AC) en la que la computadora puede usar (DC).
    
- **Ejemplo de uso**: Si conectas una GPU potente, la PSU le da la energía necesaria para funcionar sin apagar la PC.
    
- **Categorías**:
    
    - **80 Plus**: eficiencia energética (Bronze, Silver, Gold, Platinum, Titanium).
        
    - **Potencia (Wattage)**: indica cuánta energía puede dar.
        
    - **Modular / Semi-Modular / No modular**: cómo se conectan los cables a la fuente.
        



## 🔹 Placa base (Motherboard)

- **Función**: Conecta todos los componentes y permite que se comuniquen.
    
- **Ejemplo de uso**: La RAM se comunica con el CPU a través del motherboard; la GPU envía la imagen al monitor.
    
- **Partes importantes**:
    
    - **Chipset**: controla cómo se comunican CPU, RAM, disco y expansión.
        
    - **Puertos**: USB, HDMI, DisplayPort, Ethernet, PCIe, SATA.
        
    - **Slots de expansión**: para tarjetas de sonido, tarjetas de red, GPU adicional.
        
    - **BIOS/UEFI**: configuración de hardware, fechas, prioridad de arranque.
        



## 🔹 Sistema de enfriamiento

- **Función**: Evita que los componentes se sobrecalienten y se dañen.
    
- **Ejemplo de uso**: Un CPU a alta carga genera mucho calor; los ventiladores y disipadores mantienen la temperatura segura.
    
- **Tipos**:
    
    - Ventiladores estándar, disipadores de aluminio/cobre, refrigeración líquida.
        



## 🔹 Otros componentes importantes

- **Tarjeta de red (NIC)**: conecta a Internet o redes locales.
    
    - Ejemplo: Ver un video en YouTube.
        
- **Tarjeta de sonido**: procesa audio más avanzado que el integrado.
    
    - Ejemplo: Producción musical o sonido 7.1 en juegos.
        
- **Cables y conectores**: permiten la comunicación y alimentación entre todos los dispositivos.
    
- **Sensores**: temperatura, ventiladores, energía; permiten que el software controle seguridad y rendimiento.