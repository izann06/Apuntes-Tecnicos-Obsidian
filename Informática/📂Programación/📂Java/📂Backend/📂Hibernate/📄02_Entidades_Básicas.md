## 1. ¿Qué es una Entidad?

Una **Entidad** es una clase normal de Java (POJO) que representa una tabla en la base de datos.

- Cada **objeto** de la clase = Una **fila** en la tabla.
    
- Cada **atributo** de la clase = Una **columna** en la tabla.
    

Para que Hibernate sepa que esa clase es especial, le ponemos "pegatinas" (Anotaciones) que empiezan por `@`.

> **Nota importante:** En las versiones nuevas de Hibernate (6+), las importaciones vienen de `jakarta.persistence.*`. En versiones viejas era `javax.persistence.*`.

---

## 2. Las Anotaciones Sagradas

Estas son las 4 etiquetas que usarás el 90% del tiempo:

1. **`@Entity`**: Le dice a Hibernate: "Oye, esta clase se tiene que guardar en la base de datos".
    
2. **`@Table(name = "nombre_tabla")`**: Opcional, pero muy recomendada.
    
    - Si no la pones, Hibernate asume que la tabla se llama igual que la clase (`Autor` -> tabla `Autor`).
        
    - **Truco PostgreSQL:** Postgres prefiere las tablas en **minúsculas**. Si tu clase es `Autores`, pon `@Table(name="autores")` para evitar problemas.
        
3. **`@Id`**: **OBLIGATORIA**. Marca cuál es la Clave Primaria (Primary Key). Sin esto, Hibernate no funciona.
    
4. **`@Column(...)`**: Para personalizar la columna.
    
    - `name`: Si quieres que en Java se llame `nombre` pero en la BD `nom_autor`.
        
    - `length`: Para `VARCHAR(50)`.
        
    - `nullable`: `true` o `false` (NOT NULL).
        

---

## 3. Ejemplo Práctico: La clase `Autores`

Fíjate en cómo "decoramos" la clase.



```Java
package es.tuproyecto.modelos;

import jakarta.persistence.*; // Importa todas las anotaciones
import java.io.Serializable;

@Entity
@Table(name = "autores") // Forzamos minúsculas para Postgres
public class Autor implements Serializable {

    // --- ATRIBUTOS ---

    @Id // Esto es la Primary Key
    @Column(name = "cod", length = 5, unique = true, nullable = false)
    private String codigo;

    @Column(name = "nombre", length = 60)
    private String nombre;

    // --- CONSTRUCTORES (REGLA DE ORO) ---
    
    // 1. Constructor VACÍO: OBLIGATORIO para Hibernate. 
    // Lo usa para crear el objeto antes de rellenarlo.
    public Autor() {
    }

    // 2. Constructor con datos: Para que tú lo uses cómodamente.
    public Autor(String codigo, String nombre) {
        this.codigo = codigo;
        this.nombre = nombre;
    }

    // --- GETTERS Y SETTERS ---
    // Hibernate los necesita para leer y escribir en los atributos privados.
    
    public String getCodigo() { return codigo; }
    public void setCodigo(String codigo) { this.codigo = codigo; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
}
```

---

## 4. Tipos de Generación de ID

En el ejemplo anterior, el ID es un `String` (ej: "WSHAK") que tú escribes a mano. Pero, ¿y si queremos un **autonumérico** (1, 2, 3...)?

Usamos la etiqueta `@GeneratedValue`.



```Java
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY) // Como el SERIAL de Postgres
private int id;
```

- **IDENTITY:** La base de datos decide el número (el típico autoincrement). Es lo más común en MySQL y Postgres modernos.
    
- **AUTO:** Hibernate elige la mejor estrategia (a veces crea tablas extra de secuencias, cuidado).
    

---

## 5. El paso final: Registrar la clase

No basta con crear el archivo `.java`. Tienes que presentárselo a Hibernate en el archivo de configuración (`hibernate.cfg.xml`) que vimos en el tema anterior.

En `class` tienes que poner la ruta donde está tu archivo modelo,por ejemplo en mi caso es este:

```XML
<mapping class="es.accesoDatos.mp3.modelo.Artista"/> 
<mapping class="es.accesoDatos.mp3.modelo.Genero"/>  
<mapping class="es.accesoDatos.mp3.modelo.Album"/>  
<mapping class="es.accesoDatos.mp3.modelo.Track"/>
```

![[📄02_Entidades_Básicas.png]]

Si se te olvida esta línea, te saldrá el error: `Unknown entity: es.tuproyecto.modelos.Autor`.
