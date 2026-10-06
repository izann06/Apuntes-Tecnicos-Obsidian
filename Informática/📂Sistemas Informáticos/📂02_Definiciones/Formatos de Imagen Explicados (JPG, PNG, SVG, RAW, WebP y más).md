#sistemas #multimedia #formatos-imagen #jpg #png #svg #webp #raw #fotografia

> [!info] Navegación
> 📂 Carpeta: [[📂Sistemas Informáticos/📂02_Definiciones|Definiciones y Conceptos]]

---

# Todos los Formatos de Imagen Explicados

Cada formato de imagen existe por una razón concreta. No hay un formato "mejor para todo": cada uno resuelve un problema específico. Entenderlos te permite elegir correctamente en cada situación.

---

## 🔑 Conceptos Previos: Compresión

Antes de los formatos, hay que entender la diferencia fundamental:

> [!note] Compresión con pérdida vs. sin pérdida
> - **Con pérdida (Lossy):** Al comprimir, se descartan datos permanentemente. El archivo resultante es más pequeño pero **pierde calidad irreversiblemente** respecto al original.
> - **Sin pérdida (Lossless):** La compresión es matemáticamente reversible. El archivo comprimido puede descomprimirse para recuperar **exactamente el original**, bit a bit.

---

## 📸 Formatos de Mapa de Bits (Rasterizados)

### BMP — Bitmap (1988, Microsoft)

El formato más básico posible. Almacena el color de cada píxel individual **sin ninguna compresión**.

- **Tamaño:** Enorme. Una imagen 4K en BMP puede pesar 25 MB. La misma imagen en JPG: 4-8 MB.
- **Calidad:** Perfecta (no hay compresión).
- **Uso actual:** Prácticamente ninguno para el usuario final. Sigue usándose internamente en procesos de Windows y en hardware embebido que no puede manejar decodificación de JPG/PNG.

---

### JPG / JPEG — Joint Photographic Experts Group (1992)

El formato dominante para fotografías. Usa compresión **con pérdida** basada en cómo percibe el ojo humano.

- **Algoritmo:** DCT (Discrete Cosine Transform) → divide la imagen en bloques de 8x8 píxeles y descarta las frecuencias que el ojo humano percibe menos.
- **El tradeoff:** A mayor compresión (menor calidad, 1-100%), menor tamaño de archivo pero más artefactos visibles (especialmente en bordes nítidos y transiciones bruscas).
- **Cuándo usarlo:** Fotografías, imágenes para web donde el tamaño importa, redes sociales.
- **Cuándo NO usarlo:** Imágenes con texto, líneas nítidas, logotipos → el JPG introduce artefactos muy visibles en estos casos.

> [!warning] El problema de las generaciones JPG
> Cada vez que abres y guardas un JPG, la compresión se aplica de nuevo. Guardar 10 veces la misma foto degrada notablemente la calidad. **Trabaja siempre sobre el RAW o PNG original** y exporta a JPG solo la versión final.

---

### PNG — Portable Network Graphics (1996)

La alternativa sin pérdida al JPG, diseñada para reemplazar al GIF con más color y sin royalties.

- **Compresión:** DEFLATE (sin pérdida).
- **Canal alfa:** Soporte nativo de **transparencia** (canal alfa de 8 bits → 256 niveles de transparencia).
- **Cuándo usarlo:** Logotipos, iconos, capturas de pantalla, cualquier imagen con transparencia, imágenes que van a editarse más veces.
- **Desventaja:** Archivos más grandes que JPG para fotografías.

---

### GIF — Graphics Interchange Format (1987)

El abuelo de las imágenes web. Limitado pero con una característica única: **animaciones**.

- **Paleta de color:** Solo **256 colores** por fotograma (8 bits). Completamente insuficiente para fotografías.
- **Animaciones:** Múltiples fotogramas en un solo archivo → el GIF animado.
- **Transparencia:** Solo 1 bit (un color es transparente o no, sin semitransparencia).
- **Estado actual:** Obsoleto para imágenes estáticas. Para animaciones, WebP animado y AVIF lo superan técnicamente, pero el ecosistema de GIFs culturalmente sigue siendo enorme.

---

### TIFF — Tagged Image File Format (1986)

El estándar profesional para impresión y escaneado de alta fidelidad.

- **Compresión:** Generalmente sin pérdida o sin compresión alguna.
- **Profundidad de color:** Soporte para 16 bits por canal (vs. 8 en JPG/PNG).
- **Tamaño:** Archivos enormes (una foto de cámara en TIFF sin comprimir puede pesar 80-150 MB).
- **Uso:** Impresión profesional (revistas, fotografía de producto), escaneado de documentos, archivado de masterizados.

---

### WebP (2010, Google)

Diseñado para ser el sucesor del JPG y PNG en la web.

- **Soporte:** Compresión con pérdida (mejor que JPG) y sin pérdida (mejor que PNG), ambas en el mismo formato.
- **Resultado:** Archivos típicamente 25-35% más pequeños que JPG a la misma calidad visual.
- **Transparencia:** Sí, al igual que PNG.
- **Animaciones:** Sí, como GIF pero mucho mejor calidad y menor tamaño.
- **Adopción:** Soportado por todos los navegadores modernos. El formato preferido para imágenes web actualmente.

---

### AVIF (2019)

El sucesor del WebP, basado en el códec de vídeo AV1.

- **Compresión:** Significativamente mejor que WebP y JPG. Archivos hasta 50% más pequeños que JPG a igual calidad.
- **HDR:** Soporte nativo de High Dynamic Range y amplio espacio de color.
- **Desventaja:** Codificación lenta. Para imágenes generadas en tiempo real en servidor, puede ser un cuello de botella.
- **Adopción:** Creciente. Chrome, Firefox y Safari ya lo soportan.

---

### HEIC / HEIF — High Efficiency Image Container (2017)

El formato nativo de fotografías en dispositivos Apple (iPhone desde iOS 11).

- **Basado en:** El contenedor del códec de vídeo HEVC (H.265).
- **Ventaja:** Mitad de tamaño que JPG a la misma calidad percibida. Soporte de imagen en ráfaga, Live Photos y profundidad de campo en un solo archivo.
- **Problema de compatibilidad:** Windows y Android no lo soportan nativamente. Se necesita software adicional o conversión a JPG.

---

### RAW — Datos Brutos del Sensor

No es un formato único: cada fabricante tiene el suyo (Canon `.CR3`, Nikon `.NEF`, Sony `.ARW`, Adobe `.DNG`).

- **Qué contiene:** Los datos directos del sensor fotográfico **sin ningún procesamiento**. Es el "negativo digital".
- **Ventaja:** Control total en posproducción. Puedes ajustar exposición, temperatura de color y recuperar luces y sombras de forma no destructiva.
- **Desventaja:** Archivos enormes (20-80 MB por foto) y no visualizable sin software específico (Lightroom, Capture One, RawTherapee).

> [!tip] RAW vs JPG en fotografía
> El JPG que genera la cámara es el resultado de aplicar la curva de procesamiento del fabricante al RAW. Si disparas en JPG, ya no hay margen de recuperación. Si disparas en RAW, tienes toda la información para tomar decisiones en posproducción.

---

## 🎨 Formatos Vectoriales

### SVG — Scalable Vector Graphics (2001, W3C)

En lugar de almacenar píxeles, un SVG almacena **instrucciones matemáticas**: "dibuja un círculo de radio 50 en la posición X,Y con color #FF0000".

- **Escalabilidad infinita:** Un SVG puede mostrarse en una tarjeta de visita o en una valla publicitaria sin perder un ápice de calidad.
- **Tamaño:** Archivos muy pequeños para gráficos simples (un logo puede pesar 2-5 KB).
- **Editable:** Es XML, se puede editar con cualquier editor de texto.
- **Cuándo usarlo:** Logotipos, iconos, ilustraciones, gráficos para web que deben funcionar en cualquier resolución.
- **Cuándo NO usarlo:** Fotografías o imágenes con mucho detalle de textura.

---

## 🔧 Formatos de Trabajo y de Sistema

### PSD — Adobe Photoshop Document

Formato de trabajo de Photoshop. Guarda la imagen con todas sus **capas, máscaras, ajustes y efectos editables**.

- **No es un formato final:** El PSD es el "proyecto", no el resultado. El resultado final se exporta a JPG, PNG o PDF.
- **Tamaño:** Puede ser enorme (varios GB en proyectos complejos).

### ICO / ICNS

Contenedores especializados para **iconos de sistemas operativos**. Almacenan múltiples versiones de la misma imagen a distintas resoluciones (16x16, 32x32, 64x64, 128x128...) para que el SO elija la más apropiada.

- **ICO:** Windows.
- **ICNS:** macOS.

---

## 📊 Tabla Decisional Rápida

| Situación | Formato recomendado |
|---|---|
| Fotografía para web | **WebP** (o JPG si no hay soporte WebP) |
| Logo con fondo transparente | **PNG** o **SVG** |
| Fotografía para edición profesional | **RAW → exportar a TIFF** |
| Animación para web | **WebP animado** o **AVIF** |
| Icono escalable para web | **SVG** |
| Impresión profesional | **TIFF** |
| iPhone / iOS | **HEIC** (nativo) |
| Compatibilidad máxima | **JPG** (universal) |
