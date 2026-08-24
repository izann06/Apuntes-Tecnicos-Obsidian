## 1. ¿Por qué `Statement` no es lo más correcto?

En el archivo anterior vimos cómo pegar trozos de texto para crear una sentencia SQL: `"INSERT INTO tabla VALUES ('" + nombre + "')"`

Esto tiene 3 problemas graves:

1. **Es inseguro:** Un hacker puede meter código malicioso en la variable `nombre` (Inyección SQL) y borrarte la base de datos.
    
2. **Es lento:** La base de datos tiene que "leer y entender" (compilar) la sentencia cada vez que la lanzas.
    
3. **Es difícil de leer:** Te vuelves loco con tantas comillas simples `'` y dobles `"`.
    

## 2. La solución: `PreparedStatement`

`PreparedStatement` es una **plantilla**. Le envías a la base de datos la estructura de la orden _con huecos_ para rellenar después.

Los huecos se representan con interrogaciones `?`.

### Ventajas clave para examen:

- **Seguridad:** Separa el código de los datos. Lo que pongas en el hueco se trata solo como texto, nunca como código ejecutable.
    
- **Rendimiento:** La base de datos "precompila" la sentencia una sola vez. Si tienes que insertar 1000 usuarios, es muchísimo más rápido.
    

---

## 3. ¿Cómo se usa? (Sintaxis)

El proceso cambia ligeramente respecto al `Statement` normal. Fíjate bien en el orden:

1. **Defines la SQL con interrogaciones (`?`):**
    
    ```Java
    String sql = "INSERT INTO Alumnos (nombre, edad) VALUES (?, ?)";
    ```
    
2. **Preparas la sentencia (precompilación):**
    
    ```Java
    PreparedStatement ps = con.prepareStatement(sql);
    ```
    
3. **Rellenas los huecos (Setters):**
    
    - ¡OJO! Los índices empiezan en **1**, no en 0.
        
    - El método depende del tipo de dato (`setString`, `setInt`, `setDate`, etc.).
    
    ```Java
    ps.setString(1, "Ana"); // Primer interrogante
    ps.setInt(2, 25);       // Segundo interrogante
    ```
    
4. **Ejecutas:**
    
    - ¡IMPORTANTE! Aquí **NO** se pasa la SQL dentro del paréntesis, porque ya se la diste antes.
    
    ```Java
    ps.executeUpdate(); // Vacío dentro
    ```
    

---

## 4. Ejemplo Comparativo: Inserción de datos

Imagina que queremos guardar el alumno "O'Connor" (con una comilla en el nombre).

### La forma "Mala" (Statement)

Falla porque la comilla del nombre rompe la SQL.

```Java
String nombre = "O'Connor";
// ¡ERROR! La SQL se corta en la 'O'
String sql = "INSERT INTO Alumnos VALUES ('" + nombre + "')"; 
st.executeUpdate(sql); 
```

### La forma "Buena" (PreparedStatement)

Funciona perfecto y es más limpio.

```Java
String nombre = "O'Connor";
String sql = "INSERT INTO Alumnos (nombre) VALUES (?)";

try (Connection con = Conexion.conectar();
     PreparedStatement ps = con.prepareStatement(sql)) {

    ps.setString(1, nombre); // Java se encarga de "escapar" la comilla
    ps.executeUpdate();      // Guardado

} catch (SQLException e) {
    e.printStackTrace();
}
```