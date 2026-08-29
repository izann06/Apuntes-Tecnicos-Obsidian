## 1. ¿Qué es ROOM?

**ROOM** es la librería oficial de Google para guardar datos en el dispositivo. Forma parte de la suite **Android Jetpack**.

Aunque por debajo utiliza **SQLite** (la base de datos que llevan todos los móviles Android), ROOM actúa como una **capa de abstracción** (un intermediario).

> [!NOTE] Analogía
> 
> - **SQLite** es el motor del coche (potente pero complejo de manipular directamente).
> 
> - **ROOM** es el volante y los pedales (una interfaz segura y fácil para conducir ese motor).
> 

---

## 2. Ventajas frente a SQLite tradicional

El temario destaca cuatro puntos clave por los que ROOM es superior a la forma antigua de trabajar (`SQLiteDatabase`, `Cursor`, `ContentValues`):

1. **Tipado Seguro (Compile-time verification):**
 
 - _Antes:_ Si escribías `SELEC * FROM usuarios` (con error tipográfico), la app fallaba cuando el usuario la estaba usando (Crash en tiempo de ejecución).
 
 - _Con ROOM:_ Si te equivocas en la consulta SQL, **la app no compila**. Android Studio te avisa del error antes de que generes el APK.
 
2. **Integración con Arquitectura Moderna (MVVM):**
 
 - ROOM está diseñado para devolver datos observables (**LiveData** o **Flow**).
 
 - Esto permite que la Base de Datos "avise" automáticamente a la Pantalla cuando hay cambios, sin tener que estar consultando todo el rato.
 
3. **Adiós al "Boilerplate" (Código repetitivo):**
 
 - _Antes:_ Tenías que escribir cientos de líneas para convertir un objeto `Cursor` (lo que devuelve la BD) en un objeto `Usuario`.
 
 - _Con ROOM:_ Esto se hace automático. Tú le das la clase y él se encarga de "mapear" los datos.
 
4. **Migraciones Controladas:**
 
 - Facilita mucho la gestión de versiones. Si añades una columna nueva a una tabla en una actualización de la app, ROOM te ayuda a gestionar ese cambio para que el usuario no pierda sus datos antiguos.
 

---

## 3. La Regla de Oro: El Hilo Principal (Main Thread)

Hay una restricción técnica crítica que debes memorizar:

> [!DANGER] PROHIBIDO EN LA UI **ROOM no permite realizar operaciones en el hilo principal (Main Thread).**

**¿Por qué?** Leer y escribir en el disco duro del móvil es una operación "lenta" (puede tardar milisegundos o segundos si hay muchos datos). Si haces esto en el hilo donde se dibujan los botones y las animaciones, la aplicación se congelará y el sistema mostrará el temido error **ANR** (_Application Not Responding_).

**Solución:** Siempre debemos usar mecanismos asíncronos para hablar con la base de datos:

- **Corrutinas (`suspend`):** Para insertar, borrar o actualizar.
 
- **Flow / LiveData:** Para leer datos y recibir actualizaciones.