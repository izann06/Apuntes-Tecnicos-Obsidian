## 1. Conceptos Básicos

Una vez tenemos la conexión (`Connection`), necesitamos un objeto que haga de mensajero para llevar nuestras órdenes SQL a la base de datos. Ese objeto es el **Statement**.

Hay dos tipos de órdenes principales que podemos dar:

1. **DML (Data Manipulation Language):** Manipular datos (Insertar, Actualizar, Borrar).
    
2. **DQL (Data Query Language):** Consultar datos (Select).
    

> **Regla de oro:** Java usa métodos _distintos_ según el tipo de orden. Si te equivocas, el programa falla.

---

## 2. Los dos métodos sagrados

Para ejecutar SQL desde un objeto `Statement`, tienes que elegir entre estos dos métodos. 

### A) `.executeUpdate("SQL")`

- **¿Para qué sirve?** Para todo lo que **cambia** la base de datos: `INSERT`, `UPDATE`, `DELETE` (y también crear tablas con `CREATE`).
    
- **¿Qué devuelve?** Un número entero (`int`).
    
    - Ese número te dice **cuántas filas han sido afectadas**.
        
    - Si es `0`, es que no ha pasado nada (o era una instrucción de crear tabla).
        
    - Si es `1` o más, es que ha funcionado.
        

### B) `.executeQuery("SQL")`

- **¿Para qué sirve?** Exclusivamente para **consultas** (`SELECT`).
    
- **¿Qué devuelve?** Un objeto **`ResultSet`**.
    
    - El `ResultSet` es una tabla virtual con los resultados que ha encontrado.
        

---

## 3. Ejemplo práctico: Modificar datos (INSERT/UPDATE)

Aquí usamos `executeUpdate`. Fíjate que no recuperamos datos, solo queremos saber si se ha guardado.


```Java
// 1. Creamos el mensajero
Statement st = con.createStatement();

// 2. Definimos la orden SQL (OJO: Aquí estamos "pegando" strings, es la forma básica)
String sql = "INSERT INTO personas (nombre, email) VALUES ('Pepe', 'pepe@gmail.com')";

// 3. Ejecutamos
int filasAfectadas = st.executeUpdate(sql);

// 4. Comprobamos
if (filasAfectadas > 0) {
    System.out.println("¡Éxito! Se ha guardado el usuario.");
} else {
    System.out.println("Algo ha fallado, no se guardó nada.");
}
```

---

## 4. Ejemplo práctico: Leer datos (SELECT)

Aquí usamos `executeQuery`. La base de datos nos devuelve un paquete de datos (`ResultSet`) y tenemos que abrirlo fila por fila.

### El cursor del ResultSet

Imagina el `ResultSet` como una hoja de cálculo. Al principio, el "dedo" (cursor) apunta **antes** de la primera fila.

- `rs.next()`: Mueve el dedo a la siguiente fila. Devuelve `true` si hay datos, o `false` si se ha acabado la tabla.
    
- `rs.getString("columna")`: Lee el dato de la columna donde está el dedo ahora mismo.
    



```Java
Statement st = con.createStatement();
String sql = "SELECT nombre, email FROM personas";

// Ejecutamos y guardamos el resultado
ResultSet rs = st.executeQuery(sql);

// Mientras haya filas siguientes... (rs.next() devuelve true)
while (rs.next()) {
    // Leemos los datos de LA FILA ACTUAL
    String nombre = rs.getString("nombre"); // También se puede poner el índice: rs.getString(1)
    String email = rs.getString("email");
    
    System.out.println("Usuario encontrado: " + nombre + " - " + email);
}

// Al salir del bucle, el ResultSet se ha terminado.
rs.close(); // Importante cerrar
```

---

## 5. Resumen visual

| **Acción SQL** | **Método Java**   | **Retorno**       | **Ejemplo de uso**           |
| -------------- | ----------------- | ----------------- | ---------------------------- |
| **SELECT**     | `executeQuery()`  | `ResultSet`       | Leer lista de alumnos        |
| **INSERT**     | `executeUpdate()` | `int` (filas)     | Guardar un alumno nuevo      |
| **UPDATE**     | `executeUpdate()` | `int` (filas)     | Cambiar la nota de un alumno |
| **DELETE**     | `executeUpdate()` | `int` (filas)     | Borrar un alumno             |
| **CREATE**     | `executeUpdate()` | `int` (siempre 0) | Crear la tabla al inicio     |