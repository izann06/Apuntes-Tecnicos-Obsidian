El **Modelo** es la capa que representa la realidad de nuestra base de datos en código C#. No tiene lógica de botones ni sabe que existe una interfaz visual; su única misión es describir los datos.

### 📄 4.1 La Clase de Entidad (Telefono.cs)

Esta clase es el "plano" de nuestra tabla en SQL Server. Cada propiedad de esta clase será una columna en la base de datos.

- **Data Annotations (Etiquetas):** Usamos etiquetas como `[Key]` para decirle a C# cuál es la clave primaria, o `[StringLength(30)]` para limitar el tamaño del texto. Esto asegura que los datos sean correctos antes de guardarlos.
 ![[Pasted image 20251231021509.png]]

### 📄 4.2 El Contexto (AgendaDbContext.cs)

Es el archivo más importante para la persistencia. Es el **túnel** que conecta tu programa con SQL Server.

- **DbSet:** Es una propiedad que representa la tabla física. Al declarar 

- ![[Pasted image 20251231021546.png]]

- le estamos diciendo a Entity Framework: Quiero poder hacer consultas sobre la tabla de Teléfonos usando la clase Telefono.
 
- **OnConfiguring:** Aquí es donde ponemos la **Connection String** (la dirección de la base de datos). Es el carnet de identidad que permite al programa entrar en el servidor SQL.
 ![[Pasted image 20251231021618.png]]

---
