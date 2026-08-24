#  Los pasos de la Conexión a la BD

Como hemos visto anteriormente a partir de **Java 6** ya no hace falta implementar el driver.

Ahora tenemos que definir la **URL, Usuario y Contraseña**.

# 1. Tenemos que decirle _dónde_ está la base de datos. La estructura de la URL es vital: 
`jdbc:gestorBD://ordenador:puerto/nombre_base_datos`

- **URL:** `"jdbc:postgresql://localhost:5432/datos1"` (Localhost es tu PC, 5432 es el puerto estándar de Postgres).
- Donde pone postgresql ahi pones tu Gestor de Base de Datos,si usas MySql pon ese.
    
- **User:** `"postgres"`
    
- **Pass:** `"tupassword"`

```java
private static final String URL = "jdbc:postgresql://localhost:5432/music_library";  
private static final String USER = "postgres";  
private static final String PASS = "1234";
```

# 2. Después estableces la conexión:

```java
Connection con = DriverManager.getConnection(url, usuario, password); 
```

# 3.Dependencias en el Pom.xml

```java
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.7.2</version> 
</dependency>
```



Aquí tienes un ejemplo sencillo, para ver toda la estructura:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class PruebaConexion {
    public static void main(String[] args) {
        
        // Datos de conexión (Hardcodeados por ahora)
        String url = "jdbc:postgresql://localhost:5432/datos1";
        String usuario = "postgres";
        String password = "pwd";

        try {
        
            // Conectar
            Connection con = DriverManager.getConnection(url, usuario, password);
            System.out.println("¡Conexión existosa!");

            // ... Aquí haríamos las consultas ...

            //Cerrar siempre (muy importante para no dejar procesos zombies)
            //Esto se puede hacer con Try-With-Resources,automáticamente
            con.close();

        } catch (ClassNotFoundException e) {
            System.out.println("Error: No encuentro el Driver. ¿Has añadido el .jar?");
            e.printStackTrace();
        } catch (SQLException e) {
            System.out.println("Error: Fallo en SQL o conexión");
            e.printStackTrace();
        }
    }
}
```

Esto es recomendable que lo hagas en una clase aparte para no estar repitiendo ese código una y otra vez, te dejo la clase ya preparada y como se implementaría.

```java
import java.sql.Connection;  
import java.sql.DriverManager;  
import java.sql.SQLException;  
  
public class Conexion {  
    
    private static final String URL = "jdbc:postgresql://localhost:5432/music_library";  
    private static final String USER = "postgres";  
    private static final String PASS = "1234";  
  
    public static Connection conectarConexion() throws SQLException {  
        return DriverManager.getConnection(URL, USER, PASS);  
    }  
}
```

**IMPLEMENTACION:**

No tienes porque usar el `PreparedStatement` es un ejemplo, pero es para que se vea lo de Connection.

```java
try(Connection conn = Conexion.conectarConexion();  
    PreparedStatement ps = conn.prepareStatement(sql))
```