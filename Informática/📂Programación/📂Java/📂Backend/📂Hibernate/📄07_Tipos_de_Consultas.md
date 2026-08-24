## 1. Native Queries (Consultas Nativas)

Si no quieres que Hibernate te traduzca nada, escribes la consulta tal cual la pondrías en tu base de datos (Postgres, MySQL, etc.).

- **¿Cuándo se usa?** Cuando necesitas funciones raras de tu base de datos que Hibernate no entiende bien o cuando quieres optimizar al máximo una consulta muy compleja.
    
- **La diferencia clave:** Aquí usas el **nombre de la TABLA** (minúsculas, con guiones, como esté en SQL), no el de la Clase Java.
    

**Ejemplo en el código:**

```Java
// Escribimos SQL de toda la vida
String sql = "SELECT * FROM libros WHERE titulo LIKE :nombre";

List<Libros> lista = session.createNativeQuery(sql, Libros.class)
    .setParameter("nombre", "M%") // Los libros que empiecen por M
    .getResultList();
```

---

## 2. Named Queries (Consultas con Nombre)

Son consultas "pre-cocinadas". En lugar de escribir el texto de la consulta dentro del DAO (que queda muy sucio), las dejas definidas **arriba de tu Entidad** con un nombre.

- **¿Por qué son más útiles?** Porque el DAO queda limpísimo. Solo llamas a la consulta por su nombre y te olvidas del código SQL/HQL. Además, Hibernate las comprueba al arrancar, así que si te has equivocado en una letra, te avisa antes de que alguien use la App.
    

**Así se definen (en la clase Libros.java):**

```Java
@Entity
@NamedQueries({
    @NamedQuery(name = "Libros.findAll", query = "SELECT l FROM Libros l"),
    @NamedQuery(name = "Libros.findByTitulo", query = "SELECT l FROM Libros l WHERE l.titulo = :t")
})
public class Libros { ... }
```

**Así se usan (en el DAO):**

```Java
// ¡Mira qué limpio queda el código!
Query q = session.getNamedQuery("Libros.findByTitulo");
q.setParameter("t", "El Quijote");
List<Libros> resultados = q.list();
```

---

## 3. Resumen: ¿Cuál elegir?

|Tipo|¿Dónde se escribe?|¿Qué lenguaje usa?|Ventaja|
|---|---|---|---|
|**HQL (Normal)**|En el DAO.|HQL (Objetos).|Es el estándar y más sencillo.|
|**Native Query**|En el DAO.|**SQL Nativo**.|Potencia total. Usas trucos de tu BBDD.|
|**Named Query**|**En la Entidad**.|HQL o SQL.|Reutilizable, ordenado y rápido.|

---

### 💡 Un consejo:

Si estás en un proyecto de clase, intenta usar siempre **HQL** o **Named Queries**. Las **Native Queries** déjalas solo para cuando el profe te pida algo muy loco que no sepas hacer con objetos. A los puristas de Hibernate no les gusta mucho ver SQL nativo si no es estrictamente necesario.