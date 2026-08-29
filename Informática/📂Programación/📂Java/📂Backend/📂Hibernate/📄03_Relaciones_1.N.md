**Ejemplo:** Un **Autor** escribe muchos **Libros**.

- En la BBDD, la tabla `libros` tiene una columna `codautor` (la clave foránea o FK).
 
- En Java, necesitamos conectar las dos clases.
 

### A. En la clase "Muchos" (Libros) -> La que tiene la FK

Esta es la parte que manda en la base de datos porque tiene la columna física de la relación.

```Java
@ManyToOne(fetch = FetchType.LAZY) // Muchos libros, un autor
@JoinColumn(name = "codautor") // Así se llama la columna FK en la tabla SQL(Postgresql)
private Autores autores;
```

### B. En la clase "Uno" (Autores) -> El lado inverso

El autor no tiene una columna en la tabla con los libros, pero en Java queremos una lista para acceder a ellos.

```Java
// OJO AL MAPPEDBY: Es obligatorio.
@OneToMany(mappedBy = "autores") 
private Set<Libros> libroses = new HashSet<>(0);
```

> **El Truco del `mappedBy`:** `mappedBy = "autores"` significa: _"Yo (Autores) no controlo la relación en la base de datos. Vete a la clase `Libros` y mira su atributo llamado `autores` para saber cómo unirte"._