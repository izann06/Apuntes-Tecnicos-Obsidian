**Ejemplo:** **Autores** y **Libros** (Coautoría). Un libro tiene varios autores, un autor tiene varios libros.

En Bases de Datos Relacionales, **esto no existe directamente**. Se rompe creando una **Tabla Intermedia** (ej. `libro_autor`) que solo guarda parejas de IDs.

```sql
CREATE TABLE libro_autor (
 id_libro INT NOT NULL, 
 id_autor INT NOT NULL, 
 -- Definimos la Clave Primaria Compuesta -- Esto evita duplicados: no podemos tener dos veces el par (Libro A, Autor B) PRIMARY KEY (id_libro, id_autor), -- Definimos las Claves Foráneas (Relaciones 1:N) CONSTRAINT fk_libro FOREIGN KEY (id_libro) REFERENCES libros (id) ON DELETE CASCADE, -- Si borro el libro, se borra la relación CONSTRAINT fk_autor FOREIGN KEY (id_autor) REFERENCES autores (id) ON DELETE CASCADE -- Si borro al autor, se borra la relación );
```

### A. Configuración en la clase principal (Ej. Libros)

Aquí definimos cómo es esa tabla intermedia "invisible" en Java.

```Java
@ManyToMany(cascade = {CascadeType.PERSIST, CascadeType.MERGE}, fetch = FetchType.EAGER)
@JoinTable(
    name = "libro_autor",                 // Nombre de la tabla intermedia en SQL(ese nombre es de la tabla nueva de Postgresql)
    joinColumns = @JoinColumn(name = "id_libro"),        // Mi FK
    inverseJoinColumns = @JoinColumn(name = "id_autor")  // La FK del otro
)
private List<Autores> autores = new ArrayList<>();
```

### B. Configuración en la clase inversa (Ej. Autores)

Simplemente decimos "mira al otro lado".



```Java
@ManyToMany(fetch = FetchType.EAGER, mappedBy = "autores") // "autores" es el nombre de la lista en la clase Libros
private Set<Libros> libroses;
```

