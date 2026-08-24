En ROOM, una **Entidad** es una tabla de la base de datos. Para este proyecto usaremos dos entidades relacionadas: **Editorial** y **SuperHero**.

## 1. Entidades Simples (`@Entity`)

Usamos `@Entity` para decirle a ROOM: "Crea una tabla con estos campos".

### A. La tabla Editorial

![[Pasted image 20260114133611.png]]

### B. La tabla SuperHero

![[Pasted image 20260114133629.png]]

- **`tableName`**: Si no lo pones, la tabla se llamará igual que la clase. Es buena práctica ponerlo en minúsculas.
    
- **`autoGenerate = true`**: Android se encarga de ponerle el ID (1, 2, 3...) automáticamente.
    

---

## 2. Relaciones entre tablas (N:1)

En el mundo real, **muchos** superhéroes pertenecen a **una** editorial (ej: Spiderman y Iron Man son de Marvel). Esto es una relación **N:1**.

Para representar esto en ROOM sin complicar las entidades, creamos una **clase de apoyo**. Esta clase NO lleva la etiqueta `@Entity` porque no es una tabla nueva, es solo una "vista" que combina las dos anteriores.

### El modelo `SuperWithEditorial.kt`

![[Pasted image 20260114133715.png]]

> [!IMPORTANT] ¿Qué significan estas etiquetas?
> 
> - **`@Embedded`**: "Coge todas las columnas de SuperHero y mételas aquí dentro".
>     
> - **`@Relation`**: "Busca en la tabla Editorial el atributo `idEd` y luego en SuperHero el atributo `idEditorial` de mi superhéroe y la guardamos en editorial".
>     

---

## 3. Resumen de etiquetas del modelo

| **Etiqueta**      | **Función**                                              |
| ----------------- | -------------------------------------------------------- |
| **`@Entity`**     | Define que la clase es una tabla de la base de datos.    |
| **`@PrimaryKey`** | Define el identificador único (obligatorio).             |
| **`@Embedded`**   | Incluye los campos de un objeto dentro de otro.          |
| **`@Relation`**   | Define el vínculo entre dos tablas (Foreign Key lógica). |