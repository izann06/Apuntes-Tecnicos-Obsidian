## 1. ¿Qué es JDBC y por qué lo usamos?

Imagina que tu aplicación Java habla "Java" y la base de datos habla "SQL". No se entienden. Para que se comuniquen, necesitamos un **traductor**.

- **ODBC:** Era el estándar antiguo (usado en C/C++). **No es adecuado en Java** porque usa punteros (inseguro) y depende del sistema operativo.
    
- **JDBC (Java Database Connectivity):** Es la alternativa nativa de Java. Es una API (un conjunto de reglas) que nos permite conectar con _cualquier_ base de datos usando el mismo código Java.
    

## 2.El concepto clave el Driver

JDBC es solo la interfaz (el enchufe). Para que funcione con una base de datos concreta (Oracle, MySQL, PostgreSQL), necesitas instalar un **Driver** (o conector).

```java
Class.forName("org.postgresql.Driver");
```

> [!DANGER] IMPORTANTE
> Desde Java 6 ya no es neesario poner explícitamente el driver,java ahora tiene un mecanismo llamado **SPI (Service Provider Interface)**. Cuando tu aplicación arranca, Java escanea automáticamente todos los archivos `.jar` que has añadido al proyecto. Si encuentra un driver JDBC (como el de Postgres), lo registra él solo.

---
