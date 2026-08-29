## 1. ¿Qué necesitamos? (El `pom.xml`)

En JDBC solo necesitábamos el driver. En Hibernate necesitamos dos cosas:

1. **El Motor:** La librería de Hibernate (`hibernate-core`).
 
2. **Las Ruedas:** El driver de la base de datos (`postgresql`).
 

Abre tu `pom.xml` y asegúrate de tener estas dependencias (las versiones pueden cambiar, pero estas son estándar):



```XML
<dependencies>
 <dependency>
 <groupId>org.hibernate.orm</groupId>
 <artifactId>hibernate-core</artifactId>
 <version>6.4.4.Final</version>
 </dependency>

 <dependency>
 <groupId>org.postgresql</groupId>
 <artifactId>postgresql</artifactId>
 <version>42.7.2</version>
 </dependency>
</dependencies>
```

---

## 2. El Corazón: `hibernate.cfg.xml`

En JDBC poníamos la URL y el usuario dentro del código Java (mal). En Hibernate, **todo** se configura en un archivo XML separado.

### ¿Dónde se guarda?

## ¡OJO! Esto es vital. Tiene que ir **exactamente** en esta ruta: `src/main/resources/hibernate.cfg.xml`

![[📄01_Configuración_Inicial.png]]

Si lo pones en `java`, Hibernate no lo encontrará y te dará error.Además si no te aparece el `resource` tienes que crearlo tu mismo ahí.

### Contenido del archivo

Copia esta plantilla básica. Es la que usarás en el 99% de los proyectos.



```XML

<!DOCTYPE hibernate-configuration PUBLIC 
 "-//Hibernate/Hibernate Configuration DTD 3.0//EN" 
 "http://www.hibernate.org/dtd/hibernate-configuration-3.0.dtd"> 
 
<hibernate-configuration> 
 <session-factory> 
 <property name="connection.driver_class">org.postgresql.Driver</property> 
 <property name="connection.url">jdbc:postgresql://localhost:5432/music_library</property> 
 <property name="connection.username">postgres</property> 
 <property name="connection.password">1234</property> 
 <property name="dialect">org.hibernate.dialect.PostgreSQLDialect</property> 
 <property name="hibernate.default_schema">public</property> 
 <property name="hbm2ddl.auto">create</property> 
 <property name="hbm2ddl.auto">update</property> 
 
 <mapping class="es.accesoDatos.mp3.modelo.Artista"/> 
 <mapping class="es.accesoDatos.mp3.modelo.Genero"/> 
 <mapping class="es.accesoDatos.mp3.modelo.Album"/> 
 <mapping class="es.accesoDatos.mp3.modelo.Track"/> 
 </session-factory></hibernate-configuration>
```

Aqui tienes la sintaxis,por si cambian los espacios y tal (NO HAGAS CASO AL MAPPING):

![[📄01_Configuración_Inicial-1.png]]
---

## 3. Conceptos Clave para Entender

1. Se pone el driver de Postgresql.

2. La conexión con el gestor de bd,la ip del ordenador,el puerto de postgres, y la base de datos a la que queremos conectarnos.

3. Tu nombre delgestor de BD

4. Tu contraseña del gestor de BD.

### 5. El Dialecto (`Dialect`)

Hibernate no sabe si usas Oracle, MySQL o Postgres. El dialecto es el **traductor**.

- Si le dices `PostgreSQLDialect`, Hibernate sabe que para paginar se usa `LIMIT` y `OFFSET`.
 
- Si le dijeras `OracleDialect`, usaría `ROWNUM`.
 

## 6. hbm2ddl.auto

Esta es la gran diferencia con JDBC.

- En JDBC: Tienes que crear la tabla en pgAdmin `CREATE TABLE...`.
 
- En Hibernate: Creas la clase Java y Hibernate **crea la tabla por ti**.
 
 - `update`: Lo más seguro para desarrollar. Si añades un campo en Java, lo añade en la tabla.
 
 - `validate`: Solo comprueba que coinciden, no toca nada.
 

---

### Resumen Visual

```java

Tu Proyecto
├── pom.xml <-- Dependencias (Hibernate + Postgres)
├── src
│ ├── main
│ │ ├── java <-- Tu código (.java)
│ │ └── resources <-- ¡AQUÍ!
│ │ └── hibernate.cfg.xml <-- Configuración (URL, User, Dialecto)
```