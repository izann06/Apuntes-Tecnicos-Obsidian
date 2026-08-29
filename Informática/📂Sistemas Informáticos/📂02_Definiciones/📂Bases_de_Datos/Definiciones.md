# 💾 ¿Qué es una base de datos?

Una **base de datos** es como una **gran libreta digital** donde se guarda información.

👉 Ejemplo: 
Tienes una tienda online y guardas:

- Los usuarios (nombre, email, contraseña)
 
- Los productos (nombre, precio)
 
- Los pedidos (fecha, cliente, total)
 

Todo eso se guarda en **tablas**, como hojas de Excel.

---

# 🧮 ¿Qué es un Gestor de Base de Datos (DBMS)?

Es el **programa que maneja las bases de datos**. 
Tú no escribes los datos a mano: se lo pides a este programa.

👉 Ejemplo:

- **MySQL**, **PostgreSQL**, **SQLite**, **MongoDB**… son gestores.
 
- Le dices:
 
 `SELECT * FROM productos;`
 
 Y te devuelve todos los productos.
 
- También te deja **agregar, borrar, o modificar** información.


-------------------------------------------------

### 💾 **SQL (Structured Query Language)**

Bases de datos **relacionales**, con **tablas** (como una hoja de Excel). 
Cada tabla tiene filas y columnas, y puedes hacer **consultas** usando SQL.

**Ejemplo:**

`SELECT nombre, edad FROM alumnos WHERE nota > 7;`

➡ Busca en la tabla “alumnos” los que tengan una nota mayor que 7.

**Cuándo usarlo:**

- Cuando los datos tienen una estructura clara (clientes, facturas, productos).
 
- Cuando necesitas relaciones entre tablas.
 

**Ejemplos de SQL:**

- MySQL
 
- SQL Server
 
- PostgreSQL
 

---

### ⚡ **NoSQL (Not Only SQL)**

Bases de datos **no relacionales**, usan documentos, colecciones o grafos. 
Son más flexibles y rápidas para datos que cambian mucho o no tienen estructura fija.

**Ejemplo con MongoDB (usa JSON):**

`{ "nombre": "Izan", "edad": 20, "amigos": ["Pedro", "Laura"] }`

**Cuándo usarlo:**

- Cuando trabajas con datos grandes (Big Data, IA, redes sociales).
 
- Cuando no necesitas relaciones entre tablas.
 

**Ejemplos de NoSQL:**

- MongoDB
 
- Firebase
 
- Cassandra