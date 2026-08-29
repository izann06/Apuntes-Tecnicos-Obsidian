La clase `AppDatabase` es el corazón de ROOM. Es una clase abstracta que conecta nuestras **Entidades** con el **DAO** y se encarga de que solo exista una instancia de la base de datos abierta.

## 1. El Código (AppDatabase.kt)

![[Pasted image 20260114134726.png]]

---

## 2. Conceptos Avanzados de Configuración

### A. `@Volatile` y `synchronized`

- **`@Volatile`**: Asegura que cualquier cambio que un hilo haga en la variable `INSTANCE` sea visible inmediatamente para todos los demás hilos. Evita errores de lectura.
 
- **`synchronized(this)`**: Garantiza que si dos hilos intentan crear la base de datos al mismo tiempo, uno se espere al otro. Así evitamos crear **dos bases de datos** a la vez, lo que corrompería los datos.
 

### B. `exportSchema = true`

Al poner esto, ROOM genera un archivo JSON con la estructura de tus tablas. Es fundamental para cuando la app crezca y necesites hacer **migraciones** (pasar de la versión 1 a la 2 sin borrar los datos del usuario).

---

## 3. Estrategias de Migración

¿Qué pasa si mañana añades una columna "Edad" a la tabla SuperHero? ROOM necesita saber qué hacer con los datos que ya existen. Por lo que en la version de Database tendras que sumarle un numero al que ya tiene. Si su versión es `1` ahora tendrás que ponerle `2`.

| **Propiedad** | **Valor** | **Efecto** |
| ------------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`fallbackToDestructiveMigration`** | `true` | **¡CUIDADO!** Si cambias la versión, ROOM borra TODA la base de datos y la crea de nuevo. **Solo se usa en desarrollo**. |
| **`fallbackToDestructiveMigration`** | `false` | (Por defecto). Si cambias la versión y no has definido una migración manual, la app lanzará una excepción y se cerrará. Es más seguro para producción. |
| | | |

> [!TIP] En Desarrollo
> 
> Mientras estás aprendiendo y haciendo prácticas, deja fallbackToDestructiveMigration(true). Así, si cambias algo en el modelo, no tienes que desinstalar la app del móvil cada vez; ROOM se encarga de limpiar y actualizar.