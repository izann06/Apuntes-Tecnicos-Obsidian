## 1. La realidad: Las Bases de Datos fallan

Conectarse a una base de datos es una operación de **riesgo**. Pueden pasar mil cosas malas:

- Se ha ido internet.
    
- La contraseña ha cambiado.
    
- Intentas guardar un usuario que ya existe (clave duplicada).
    
- Te has equivocado escribiendo la SQL (`SELEC` en vez de `SELECT`).
    

Por eso, Java te obliga a rodear casi todo el código JDBC con **Try-Catch**.

---

## 2. Nivel 1: "El Vago" (Throws)

Lo que hacemos cuando estamos aprendiendo o probando rápido. Le pasamos la patata caliente a Java.



```Java
public static void main(String[] args) throws SQLException, ClassNotFoundException {
    // Código JDBC...
}
```

- **Problema:** Si algo falla, el programa **explota** (se cierra de golpe) y muestra un mensaje en rojo horrible en la consola que un usuario normal no entiende.

---

## 3. Nivel 2: El Estándar (Try-Catch genérico)

Atrapamos el error para que el programa no se cierre de golpe y mostramos un mensaje.



```Java
try {
    // Conexión y consultas...
    stmt.executeUpdate("INSERT...");

} catch (ClassNotFoundException e) {

    System.out.println("ERROR CRÍTICO: No encuentro el driver de PostgreSQL.");
    
    // Esto suele ser fallo de configuración del proyecto
} catch (SQLException e) {

    System.out.println("ERROR SQL: Algo ha fallado en la consulta o conexión.");
    
    e.printStackTrace(); // Imprime la traza técnica para el programador
}
System.out.println("El programa continúa...");
```

- **Ventaja:** El programa no se muere (`Terminado!` al final).
    
- **Desventaja:** `SQLException` es un "cajón de sastre". Ahí cae todo: desde "no hay internet" hasta "tabla no encontrada".
    

---

## 4. Nivel 3: El Pro (Diagnóstico preciso)

Aquí es donde demuestras que sabes. El objeto `SQLException` tiene métodos para saber **exactamente** qué ha pasado.

- `e.getMessage()`: El texto del error (ej: "relation 'personas' does not exist").
    
- `e.getSQLState()`: Un código estándar (5 caracteres) que te dice el tipo de error.
    
- `e.getErrorCode()`: El código específico del vendedor (Postgres).
    

### Ejemplo: Evitar duplicados sin romper

Imagina que insertamos un alumno con DNI '123'. Si ya existe, falla. Queremos avisar, no explotar.

```Java
try {
    String sql = "INSERT INTO alumnos (dni, nombre) VALUES ('123', 'Pepe')";
    stmt.executeUpdate(sql);

} catch (SQLException e) {
    // Analizamos el código de error
    // En Postgres, el estado "23505" significa "UNIQUE VIOLATION" (duplicado)
    if ("23505".equals(e.getSQLState())) {
        System.out.println("AVISO: Ese alumno ya existe. No se ha guardado.");
    } else {
        // Si es cualquier otro error (ej: conexión caída), sí que es grave
        System.out.println("Error desconocido: " + e.getMessage());
        e.printStackTrace();
    }
}
```

---

## 5. Resumen de Estados SQL (SQLState) comunes

No hace falta memorizarlos todos, pero saber que existen te salva la vida:

| **Código (aprox)** | **Significado**          | **Ejemplo**                               |
| ------------------ | ------------------------ | ----------------------------------------- |
| **08xxx**          | Error de conexión        | Servidor apagado, IP incorrecta           |
| **42xxx**          | Error de sintaxis        | Escribir `SELECCIONAR` en vez de `SELECT` |
| **23505**          | Violación de clave única | Intentar meter un ID repetido             |
| **42P01**          | Tabla no definida        | Hacer `SELECT * FROM tabla_falsa`         |

---

### Conclusión del Bloque JDBC

1. Conectamos (`Connection`).
    
2. Preparamos la orden (`PreparedStatement`).
    
3. Si es SELECT -> `executeQuery` -> `ResultSet`.
    
4. Si es INSERT/UPDATE -> `executeUpdate` -> `int`.
    
5. Todo rodeado de `try-catch` para que no explote.