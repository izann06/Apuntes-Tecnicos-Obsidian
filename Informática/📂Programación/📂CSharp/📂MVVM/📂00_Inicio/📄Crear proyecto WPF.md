
**Obligatorio**: Tienes que tener instalado VS y SQL Server Management Studio.

## **MANERA 1(CREAR LA BASE DE DATOS CON VS)**

## 🧩 1️⃣ Instalar los paquetes NuGet necesarios

Abre la **Consola del Administrador de Paquetes**:

> `Herramientas > Administrador de paquetes NuGet > Consola del Administrador de paquetes`

Y ejecuta **uno por uno** estos comandos:

`Install-Package Microsoft.EntityFrameworkCore Install-Package Microsoft.EntityFrameworkCore.SqlServer Install-Package Microsoft.EntityFrameworkCore.Tools`

✅ Esto instala los Pluggins EF Core y las herramientas para crear migraciones.

## 🧱 2️⃣ Crea tu clase `Usuario` por ejemplo

![[CodigoClaseUser.png]]


 
## 🗄️ 3️⃣ Crea tu clase `TaskManagerDbContext`

Importantísimo crear esta clase ya que es la conexión con la base de datos. 

![[ClaseTaskManagerDbContext.png]] } }`

---

## ⚙️ 4️⃣ Crear la base de datos con migración

Ahora en la **Consola del Administrador de Paquetes**, ejecuta:

`Add-Migration (Aqui pon un nombre descriptivo)
Por ejemplo: Inicio

Update-Database`

🧠 Qué hace:

- `Add-Migration crea un script con la tabla `Usuarios`.
 
- `Update-Database` crea **la base de datos Tareas_IMM** y **la tabla Usuarios** automáticamente en SQL Server LocalDB.
 

## 👤 5️⃣ Insertar un usuario

Una vez creada, abre **SQL Server Management Studio

Haces una consulta(query).
![[Pasted image 20251230190528.png]]

Este es un ejemplo:

`INSERT INTO Usuarios (UsuarioNombre, PasswordHash, NombreCompleto, CorreoElectronico, Activo) VALUES ('admin', '1234', 'Administrador del sistema', 'admin@empresa.com', 1);`

⚠️ No pongas el campo `Id` (es autonumérico).

## ✅ 6️⃣ Verificar

Comprueba en SQL Server Management Studio:
![[Select.png]]
`SELECT * FROM Usuarios;`

