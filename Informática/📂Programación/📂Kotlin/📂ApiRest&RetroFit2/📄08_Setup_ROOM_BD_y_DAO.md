Aquí es donde tu aplicación deja de ser "volátil" (si cierras, pierdes todo) y pasa a tener memoria propia. Vamos a configurar **ROOM**, que es la librería de Google para manejar bases de datos SQL de forma fácil.

---

En este archivo configuramos los cimientos de la base de datos local. Necesitamos tres piezas:

1. **Entidad:** La tabla (modificamos el `Post`).
 
2. **DAO:** Las instrucciones SQL (insertar, leer).
 
3. **Database:** La caja fuerte que contiene todo.
 

---

## 1. Modificación del Modelo (Post.kt)

Tenemos que volver al archivo que creamos al principio `data/model/Post.kt` y asignarle etiquetas de ROOM. Ahora, además de ser un objeto de Kotlin, será una tabla de SQL.

He añadido la **tabla** y la **PrimaryKey** ya está.

![[Pasted image 20260114002059.png]]

---

## 2. El DAO (PostsDAO.kt)

**DAO** significa _Data Access Object_. Es una interfaz donde definimos las operaciones que queremos hacer con la base de datos. ROOM escribirá el código SQL por nosotros basándose en estas anotaciones.

![[Pasted image 20260114002159.png]]

> [!NOTE] ¿Por qué `getPosts` no es `suspend`? Porque devuelve un `Flow`. Un Flow no es una operación de "una sola vez", es una tubería abierta ya que vamos a utilizarla muchas veces. La tubería se crea al instante (rápido), y los datos fluyen por ella después (asíncrono).En los `Select` como solemos usarlos muchos suelen ser de tipo `Flow`.

---

## 3. La Base de Datos (AppDatabase.kt)

Esta es la clase principal. Usamos el patrón **Singleton** para asegurar que nunca haya dos bases de datos abiertas a la vez, lo cual corrompería los archivos.

![[Pasted image 20260114002345.png]]

---
