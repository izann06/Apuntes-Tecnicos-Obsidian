## 1. El Ciclo de Vida General (El Director)

LibGDX está controlado por eventos del Sistema Operativo. Estos `métodos override` solo existen en las clases que heredan de `KtxGame` (Aplicación) o `KtxScreen` (Pantallas).

Por lo que no puedes usar estos métodos en otras clases.

| **Método** | **¿Cuándo se llama automáticamente?** | **¿Qué debes hacer dentro?** | Código |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------ |
| **`create()`** | **1 sola vez**, al abrir la app. (Solo donde herede `KtxGame` | Encender OpenGL. Crear cosas pesadas (`SpriteBatch`, `AssetManager`). | |
| **`show()`** | **1 sola vez**, cada vez que se abre una Pantalla. Solo donde herede `KtxScreen` | Preparar el nivel, poner el contador a 0, darle al Play a la música de fondo. | |
| **`resize()`** | Al girar el móvil o cambiar tamaño de ventana en PC. | Actualizar el `Viewport` para que la cámara no deforme la imagen. | |
| **`render()`** | **60 veces por segundo** FPS (El bucle de juego). Solo donde herede `KtxScreen` | 1º Actualizar físicas y lógica. 2º Limpiar la pantalla. 3º Dibujar imágenes. | |
| **`pause()`** | En móvil se usa al 100%.Cuando te sales del juego,se para todo,en PC no es del todo asi ya que al ser multitarea,el juego puede seguir corriendo sin problema, es más opcional digamos. | Pausar música, guardar partida en memoria. Vital en móviles. | |
| **`resume()`** | Al recuperar el foco del pause(). | Volver a darle al Play a la música, quitar el menú de pausa. | |
| **`dispose()`** | Al destruir la pantalla o cerrar el juego. Solo donde herede `KtxGame/KtxScreen` | Liberar memoria gráfica manual (`batch.dispose()`, texturas, física). | |

| **Método** | **Código** |
| --------------- | ------------------------- |
| **`create()`** | ![[📄Arquitectura-8.png]] |
| **`show()`** | ![[📄Arquitectura-7.png]] |
| **`resize()`** | ![[📄Arquitectura-5.png]] |
| **`render()`** | ![[📄Arquitectura-6.png]] |
| **`pause()`** | ![[📄Arquitectura-2.png]] |
| **`resume()`** | ![[📄Arquitectura-3.png]] |
| **`dispose()`** | ![[📄Arquitectura-4.png]] |
## 2. La Jerarquía del Proyecto (Quién es quién)

### A. La Consola (`KotlinGameMain.kt`)

- **Rol:** Memoria RAM a largo plazo y dueña del hardware.
 
- **Tareas:** Carga las imágenes, guarda las puntuaciones que no deben borrarse entre niveles, y cambia de una pantalla a otra usando `setScreen()`.

* Es donde se encuentra el create(). 
 

### B. Los Canales (`Las Screens`)

- **Rol:** Los diferentes estados visuales del juego.
 
- **Ejemplos:**
 
 - `MenuScreen`: Dibuja texto y espera un toque en la pantalla para arrancar el juego.
 
 - `LoadingScreen`: Muestra una barra mientras `assets.update()` carga los archivos pesados en segundo plano.
 
 - `GameScreen`: El monstruo final. Aquí es donde se juega.
 

### C. Las Leyes del Universo (`WorldManager.kt` y Box2D)

- **Box2D:** Motor de físicas que usa Metros, Kilos y Segundos (NO píxeles).
 
- **`WorldManager`:** Es el "Dios" de la física.
 
 - _Aplica el tiempo:_ `world.step()` hace que la gravedad funcione.
 
 - _Es el Árbitro:_ Usa el **ContactListener** para saber cuándo chocan dos cosas mirando sus etiquetas (`userData`). No puede borrar cosas durante el choque, las anota en una lista para borrarlas después.
 

### D. Los Actores (`La carpeta Entity`)

No tienen ciclo de vida automático. Tienen su propio cuerpo físico invisible (`Body`) y su propio dibujo (`Texture`).

- **Movimiento:** A los personajes de plataformas nunca se les "empuja" (Fuerza), se les da un "golpe seco" (**Impulso Lineal**) para que el movimiento sea instantáneo y perfecto.
 
- **Sensores:** Cuerpos físicos (`isSensor = true`) que el jugador puede atravesar como un fantasma (ej. Monedas), pero que el Árbitro (`ContactListener`) detecta para dar puntos.
 
- **Animación:** Una máquina de estados (`enum class Estado`) decide si el personaje se dibuja corriendo, saltando o cayendo basándose en su velocidad física actual.
 

### E. El Escenario (`MapLoader.kt`)

- Usa archivos **`.tmx`** creados en Tiled.
 
- Separa lo que el jugador _ve_ (capas de dibujo) de lo que el jugador _toca_ (capas de colisiones ocultas).
 
- Se usa **`Box2DDebugRenderer`** (Las Gafas de Rayos X) para ver si las cajas invisibles de colisión coinciden realmente con los dibujos que vemos en pantalla. Se debe dibujar _después_ de todo lo demás para que quede por encima.


### F. La Interfaz de Usuario (`La carpeta ui` / `HUD.kt`)

- **Rol:** El "cristal" de tu pantalla. Todo lo que dibujes aquí se queda fijo aunque el personaje corra y la cámara del juego se mueva.
 
- **Scene2D y Stage:** LibGDX tiene un sistema especial para hacer menús e interfaces llamado Scene2D. El `Stage` (Escenario) es el contenedor principal.
 
- **El choque de dos mundos (Viewports):** * El juego (Box2D) usa un `ExtendViewport` basado en **Metros** (por ejemplo, el mundo mide 20x11 metros).
 
 - El `HUD` usa un `ScreenViewport` basado en **Píxeles** (por ejemplo, 1080x1920 píxeles).
 
 - Por eso el HUD se dibuja **el último** en el método `render()` de la `GameScreen`, para que la puntuación y las vidas se pinten por encima de los árboles y las nubes.
 

### G. Los Efectos Visuales (`La carpeta particles` / `GestorParticulas.kt`)

- **Rol:** Darle "jugo" (game feel) al juego con polvo al saltar o destellos al coger monedas.
 
- **El problema del Garbage Collector:** Si cada vez que recoges una moneda creas 16 partículas nuevas (`Particula p = Particula()`), crearás miles de objetos por minuto. El recolector de basura de Java/Kotlin se saturará, pausará el juego para limpiar la memoria, y el jugador notará un "tirón" (lagazo).
 
- **La Solución: Object Pooling (Piscina de objetos):** Fíjate en el código de esa clase. Al principio crea una lista fija de 128 partículas (`val pool = Array(128) { Particula() }`).
 
 - En vez de crear y destruir, las partículas se **reciclan**.
 
 - Cuando una partícula desaparece, no se destruye, simplemente se le pone la etiqueta `activa = false` y se manda a "descansar al banquillo" hasta que vuelva a hacer falta para el siguiente salto.