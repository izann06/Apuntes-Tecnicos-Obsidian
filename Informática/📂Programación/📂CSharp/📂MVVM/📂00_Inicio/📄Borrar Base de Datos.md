# Pasos para borrar la BD y empezar de cero

Esto lo hago porque ya tenía implementada en la bd la tabla 'usuarios' y al querer añadir más tarde la tabla 'Tareas' tuve problemas porque al hacer (Add-Migration) porque usuarios estaba creado.
Asi que lo que hice fue borrar la base de datos e instaalrla de nuevo ya que no me importa perder los datos.

### 1️⃣ Borrar la base de datos

- Puedes hacerlo desde **SQL Server Management Studio**:
 
- Botón derecho sobre la base de datos:

![[Práctica01(WPF)Gestor_de_Usuarios_con_SQL_Server-2.png]]

- O desde **Package Manager Console**:
 
`Drop-Database`

_(Este comando borra completamente la base de datos vinculada al DbContext actual)_

---

### 2️⃣ Eliminar todas las migraciones

En tu proyecto vete a la terminal nugget en VS:

`Remove-Migration`

![[Práctica01(WPF)Gestor_de_Usuarios_con_SQL_Server-1.png]]

Repite hasta que no queden migraciones (o borra la carpeta `Migrations` completamente).
![[Práctica01(WPF)Gestor_de_Usuarios_con_SQL_Server.png]]

---

### 3️⃣ Crear migración inicial

Con tu `DbContext` ya actualizado con `DbSet<User>` y `DbSet<Tarea>`:
![[Práctica01(WPF)Gestor_de_Usuarios_con_SQL_Server-3.png]]

`Add-Migration Inicial`

- EF Core detectará todas las tablas (`Usuarios`, `Tareas`, etc.) y generará el script para crearlas.

 ![[Práctica01(WPF)Gestor_de_Usuarios_con_SQL_Server-4.png]]
 

---

### 4️⃣ Aplicar migración y crear la base de datos

`Update-Database`

- Esto creará la base de datos desde cero, con todas las tablas que tienes en tu modelo.
 
- EF Core también creará la tabla `__EFMigrationsHistory` para llevar el control de migraciones.
![[Práctica01(WPF)Gestor_de_Usuarios_con_SQL_Server-5.png]]
 

---

### ⚠️ Nota

- **Esto borra todos los datos actuales**, así que solo se recomienda si estás en desarrollo.