#sistemas #hardware #componentes-pc #cpu #gpu #ram #ssd #placa-base

> [!info] Navegación
> 📂 Carpeta: [[📂Sistemas Informáticos/📂01_Componentes PC|Componentes de PC]]

---

# Componentes del PC Explicados

Cada componente de un ordenador tiene **una función específica e insustituible**. Entender qué hace cada pieza te permite diagnosticar problemas, elegir mejor cuando compras y entender por qué un PC va lento o rápido.

---

## 🧠 CPU — Unidad Central de Procesamiento

El "cerebro" del ordenador. Su función es leer datos de la memoria, decodificarlos, ejecutarlos y escribir el resultado. Se encarga de la lógica general del sistema operativo y las aplicaciones.

- **Núcleos e Hilos (Cores/Threads):** Un núcleo físico es un procesador real independiente dentro del chip. Los hilos (gracias a tecnologías como Hyper-Threading o SMT) permiten a un núcleo físico manejar dos colas de instrucciones simultáneamente, mejorando la eficiencia en multitarea sin añadir hardware completo.
  
- **Frecuencia de Reloj (GHz):** Indica cuántos miles de millones de ciclos de instrucción se ejecutan por segundo. Una CPU a 4.0 GHz realiza 4.000 millones de ciclos/s. Sin embargo, no se puede comparar entre distintas arquitecturas solo por los GHz.
  
- **IPC (Instrucciones por Ciclo):** Mide cuánto trabajo real hace la CPU en cada uno de esos ciclos. Una CPU moderna a 3.0 GHz con alto IPC destrozará a una CPU antigua a 4.5 GHz con bajo IPC.
  
- **Caché (L1, L2, L3):** Memoria estática (SRAM) ultra-rápida y diminuta dentro del propio procesador. La CPU busca datos aquí antes de ir a la RAM. La L1 es la más rápida y pequeña (kilobytes, por núcleo), la L3 es la más lenta y grande (megabytes, compartida).
  
- **Litografía (Nanómetros - nm):** El tamaño de los transistores. A menor tamaño (ej. 3nm, 5nm), caben más transistores en el mismo espacio, la señal viaja menos distancia y se reduce el consumo energético y el calor generado.

---

## 🎮 GPU — Unidad de Procesamiento Gráfico

Mientras la CPU es como un profesor universitario brillante que resuelve problemas complejos uno a uno, la GPU es como un ejército de estudiantes de primaria resolviendo millones de sumas sencillas simultáneamente. Es un acelerador matemático diseñado para el **procesamiento paralelo masivo**.

- **Núcleos de procesamiento:** A diferencia de los 8 o 16 núcleos de una CPU, una GPU dedicada moderna (como una RTX 4090) tiene más de 16.000 pequeños núcleos (CUDA cores en NVIDIA, Stream Processors en AMD).
  
- **VRAM (Video RAM):** Memoria GDDR (ej. GDDR6X) soldada directamente en la tarjeta gráfica. Es muchísimo más rápida que la RAM del sistema porque necesita cargar texturas 4K y geometría masiva en milisegundos sin latencia.
  
  
- **Núcleos Especializados:**
  
  - **Tensor Cores:** Diseñados exclusivamente para operaciones de matrices masivas usadas en Inteligencia Artificial y Machine Learning (ej. DLSS de NVIDIA).
    
  - **RT Cores:** Dedicados exclusivamente al cálculo de intersecciones de rayos de luz para el Ray Tracing en tiempo real.
    
- **Usos modernos:** Además del renderizado de videojuegos, hoy en día las GPUs son el motor de la revolución de la IA (entrenamiento de LLMs), minería de criptomonedas, simulaciones físicas complejas y renderizado 3D (Blender, Maya).

---

## ⚡ RAM — Memoria de Acceso Aleatorio

Es el **taller o mesa de trabajo** del procesador. El disco duro es el almacén. Para trabajar en algo, el procesador saca los datos del almacén (disco) y los pone en la mesa (RAM).

- **Volatilidad:** Es memoria dinámica (DRAM) que necesita refrescarse constantemente con electricidad. Si se corta la energía, todo su contenido desaparece en microsegundos.
  
- **Latencia CAS (CL):** El tiempo (en ciclos de reloj) que tarda la RAM en responder a una petición de la CPU. Una RAM DDR4 a 3200MHz con CL16 puede ser igual de rápida en ciertas tareas que una a 3600MHz con CL18. Menor CL indica una respuesta más rápida.
  
- **Dual Channel / Quad Channel:** En lugar de comunicarse con un módulo a la vez por un bus, el controlador de memoria se comunica con dos módulos simultáneamente por canales independientes, duplicando el ancho de banda efectivo. Por eso siempre es mejor instalar dos módulos de 8GB que uno solo de 16GB.

> [!warning] El Paginado (Swap)
> ¿Qué pasa cuando abres tantas cosas que te quedas sin RAM? El sistema operativo usa una parte de tu disco duro/SSD como "RAM de emergencia" (archivo de paginación o partición Swap). Como el disco de almacenamiento es órdenes de magnitud más lento que la RAM, tu PC se congelará y se volverá extremadamente lento.

---

## 💾 Almacenamiento: HDD vs SSD

Es la memoria no volátil, donde los datos del SO, programas y archivos persisten incluso sin energía.

### HDD (Disco Duro Mecánico)

- **Funcionamiento:** Un disco de aluminio o cristal recubierto de material magnético gira a miles de RPM (5400, 7200) mientras un brazo mecánico con un cabezal de lectura/escritura "vuela" a nanómetros de la superficie magnetizando las zonas (0s y 1s).
  
- **Fragmentación:** Como el cabezal tiene que moverse físicamente, si un archivo grande se guarda en trozos separados por todo el plato, el disco tarda mucho en ir a leerlo todo. Por eso requieren desfragmentación periódica.
  
- **Ideal para:** Servidores NAS, copias de seguridad profundas (backups), almacenamiento en frío masivo donde el coste barato por Terabyte es lo principal.

### SSD (Unidad de Estado Sólido)

- **Funcionamiento:** Basado en chips de memoria NAND Flash. Un controlador integrado distribuye los datos electrónicamente entre múltiples celdas microscópicas, sin absolutamente ninguna parte móvil.
  
- **IOPS (Operaciones de Entrada/Salida Por Segundo):** La métrica clave. Mientras un HDD lee archivos pequeños muy lentamente por la limitación mecánica, un SSD lee miles de archivitos del sistema casi al instante. Esto es lo que hace que un PC "vuele" al arrancar.
  
- **TBW (Terabytes Escritos):** La esperanza de vida de un SSD. Cada vez que escribes en una celda flash, se desgasta microscópicamente. El TBW indica cuántos Terabytes puedes escribir antes de que el fabricante considere agotada su vida útil (suele ser enorme, los usuarios rara vez lo alcanzan).
  
- **Formatos y Velocidades:**
  
  - **SATA 2.5":** Limitados a ~550 MB/s por el antiguo cable de conexión SATA.
    
  - **M.2 NVMe:** Conectados directamente a los canales PCIe de la placa base, permitiendo velocidades salvajes que van de los 3.000 MB/s (Gen 3) a más de 12.000 MB/s (Gen 5).

---

## 🔌 Placa Base (Motherboard)

La espina dorsal del sistema. Es una compleja placa de circuito impreso (PCB) multicapa que conecta, energiza y enruta la información entre absolutamente todos los componentes.

- **Socket y Chipset:** El socket (ej. AM5, LGA1700) dicta físicamente qué familia de procesadores puedes encajar. El chipset (ej. B650, Z790) es un chip secundario en la placa que controla los puertos USB, las líneas SATA, el audio y parte de la red, dictando qué funciones avanzadas (como overclocking o configuraciones RAID de discos) están disponibles.
  
- **VRM (Módulo Regulador de Voltaje):** Un componente crucial y poco conocido. Convierte los ruidosos 12V que vienen de la fuente de alimentación a los ~1.2V ultra-estables y filtrados que necesita la CPU. Una CPU muy potente en una placa base barata sufrirá porque los VRM se sobrecalentarán y limitarán la entrega de energía (throttling).
  
- **Buses PCIe (Peripheral Component Interconnect Express):** Las "autopistas" de datos de alta velocidad que conectan directamente la gráfica y los SSDs NVMe ultrarrápidos con el procesador. Se miden en "líneas" (x4, x8, x16) y generaciones (Gen 3, Gen 4, Gen 5), duplicando su ancho de banda teórico con cada salto generacional.

---

## ❄️ Refrigeración

La gestión térmica es vital. El silicio pierde eficiencia al calentarse. Los procesadores modernos usan algoritmos de "boost" dinámico: cuanto más fríos operan, más suben su velocidad automáticamente para rendir más, hasta chocar con el límite térmico seguro.

- **Presión estática vs. Flujo de aire (Airflow):**
  
  - **Ventiladores de Flujo de aire (Airflow):** Aspas diseñadas para mover mucha cantidad de volumen de aire (CFM) rápidamente sin obstáculos. Ideales para extraer el aire caliente por la parte trasera de la caja.
    
  - **Ventiladores de Presión estática:** Aspas anchas y planas diseñadas para empujar aire a la fuerza a través de obstrucciones muy tupidas como los radiadores de refrigeración líquida o los bloques de aluminio de disipadores CPU.
    
- **Pasta Térmica (Thermal Paste):** Las superficies de metal de la CPU y el disipador tienen poros microscópicos. Al unirlas, el aire se queda atrapado (y el aire es un pésimo conductor del calor). La pasta térmica rellena esos poros creando un puente perfecto de transferencia térmica.
  
- **Tipos de disipación principal:**
  
  - **Aire:** Grandes torres de aletas de aluminio atravesadas por gruesos tubos de cobre (*heatpipes*). El cobre absorbe el calor, lo transfiere al aluminio, y los ventiladores lo expulsan. Super fiables porque no pueden tener fugas.
    
  - **Líquida AIO (All-in-One):** Una bomba de agua sellada de fábrica mueve líquido refrigerante continuo sobre la CPU, transportando el calor por tubos hacia un radiador grande donde múltiples ventiladores lo enfrían de golpe. Ideal para CPUs muy calientes y picos de rendimiento.

---

## ⚡ PSU — Fuente de Alimentación

El componente que da vida a todo lo demás. Convierte la peligrosa y fluctuante corriente alterna (AC 220V/110V) de tu enchufe en voltajes de corriente continua perfecta (DC 12V, 5V, 3.3V) exigidos por el hardware.

- **Protecciones de hardware integradas:** Una fuente de calidad incluye un escudo de protecciones eléctricas como OVP (contra sobrevoltajes de la red), SCP (contra cortocircuitos) y OPP (sobrecarga), diseñadas para sacrificarse a sí misma "quemando un fusible interno" para evitar que el pico eléctrico fría y mate a tu CPU o GPU de 1000€.
  
- **PFC Activo (Corrección de Factor de Potencia):** Asegura que la fuente consuma energía de la red eléctrica de tu hogar de la forma más pura y eficiente posible, evitando devolver "ruido eléctrico armónico" que podría dañar otros electrodomésticos en tu misma red eléctrica.
  
- **Certificación 80 PLUS:** Es un sello de garantía de eficiencia. Indica que al transformar la energía de la pared, al menos el 80% (o más del 90% en niveles Gold, Platinum o Titanium) se convierte en energía pura para tus piezas y no se desperdicia perdiéndose en forma de calor residual dentro de la propia fuente.

---

## 🏠 Chasis (Torre o Caja)

La caja del ordenador nunca es solo por estética. Su diseño interno dicta completamente el rendimiento térmico y acústico global del sistema. Si los componentes no respiran, se ahogarán térmicamente.

- **Factores de Forma:**
  
  - **ATX / Mid-Tower:** El estándar de escritorio más común. Espacio de sobra para tarjetas gráficas gigantes, placas base estándar y flujos de aire cómodos.
    
  - **Mini-ITX / SFF (Small Form Factor):** Ordenadores increíblemente densos del tamaño de una consola. Requieren planeación milimétrica del calor, refrigeraciones líquidas encajadas, gráficas medidas al milímetro y fuentes de alimentación miniaturizadas (SFX).
    
- **El concepto de presión del flujo de aire interno:**
  
  - **Presión Positiva:** Más ventiladores potentes *metiendo* aire fresco que sacando. El exceso de aire presurizado se ve forzado a escapar de forma natural por todas las rendijas. Es la mejor forma para mantener el PC sin polvo interno (siempre que las entradas principales tengan mallas de filtro anti-polvo).
    
  - **Presión Negativa:** Más ventiladores potentes *extrayendo* aire caliente que metiendo fresco. La caja genera un "vacío" e intentará succionar aire desesperadamente por cada rendija, tornillo o hueco sin filtrar, llenando tu PC de polvo y pelusas rápidamente. Favorece temperaturas brutas mínimamente mejores, pero a costa de mantenimiento constante.
