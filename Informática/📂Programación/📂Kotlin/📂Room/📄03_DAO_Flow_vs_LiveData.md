El **DAO** (_Data Access Object_) es la interfaz donde definimos cómo interactuar con los datos. Aquí es donde ROOM demuestra su potencia al permitirnos usar programación reactiva.

## 1. El Código del DAO (`SupersDAO.kt`)

![[Pasted image 20260114134226.png]]

---

## 2. Conceptos Clave del DAO

### A. Flow vs LiveData

- **Flow (Recomendado para Compose):** Es parte de las corrutinas de Kotlin. Es más moderno, potente y fácil de manipular con operadores.Usamos este.
    
- **LiveData:** Es la herramienta clásica de Android. Es más sencilla pero está siendo desplazada por Flow en aplicaciones modernas con Jetpack Compose.
    

### B. `@Transaction`

Se usa cuando una consulta implica varias acciones. Por ejemplo, para traer un `SuperWithEditorial`, ROOM primero busca al héroe y luego busca su editorial. Usar `@Transaction` asegura que si algo falla en medio, no se devuelvan datos incompletos.

### C. Parámetros en las consultas

Fíjate en `:idSuper`. Los dos puntos le dicen a ROOM: "Busca la variable que te paso por el parámetro de la función y ponla aquí en el SQL".
![[Pasted image 20260114134543.png]]

---

## 3. Estrategias de Conflicto (`REPLACE`)

En el `@Insert` usamos `onConflict = OnConflictStrategy.REPLACE`.

- **¿Qué hace?** Si intentas insertar un superhéroe con el ID 7 y ya existe uno con ese ID, ROOM borrará el viejo y pondrá el nuevo.
    
- **Ventaja:** Esto nos permite usar la función de "Insertar" también para "Actualizar", ahorrándonos crear una función `@Update`.