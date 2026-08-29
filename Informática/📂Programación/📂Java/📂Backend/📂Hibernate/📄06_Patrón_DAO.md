Para que lo entiendas de un vistazo: el patrón **DAO (Data Access Object)** es como un restaurante. Tienes la **Carta** (la Interfaz) donde ves qué puedes pedir, y luego tienes al **Cocinero** (la Implementación) que es el que se pelea con los fogones (la base de datos) para traerte el plato.

---

## 1. La Interfaz (`LibrosDAO`) – "La Carta"

Aquí solo escribimos los nombres de los métodos. No hay código, solo decimos **qué se puede hacer**.

- **¿Por qué una interfaz?** Porque si mañana tu jefe decide dejar de usar Hibernate y usar otra cosa, el resto de tu programa no se entera; solo tendrías que cambiar al "cocinero" (la implementación), pero la carta sigue siendo la misma.
 



```Java
public interface LibrosDAO {
 // Definimos qué queremos hacer, sin decir cómo:
 List<Libros> obtenerLibros(); // Traerlos todos
 Libros obtenerLibroPorId(int id); // Buscar uno concreto
 void insertarLibro(Libros libro); // Guardar uno nuevo
}
```

---

## 2. La Implementación (`LibrosDAOImpl`) – "El Cocinero"

Aquí es donde metemos las manos en el barro y usamos **Hibernate**. Esta clase es la que de verdad habla con la base de datos.

### ¿Qué hace el Cocinero aquí dentro?

1. **Abre la sesión:** Llama a `HibernateUtil` para pedir una conexión.
 
2. **Lanza la consulta (HQL):** Ojo, aquí no usamos SQL normal, usamos HQL (el lenguaje de Hibernate que habla con Clases, no con tablas).
 
3. **Devuelve los datos:** Transforma las filas de la base de datos en objetos Java.
 

**Ejemplo real del código:**



```Java
public class LibrosDAOImpl implements LibrosDAO {

 @Override
 public List<Libros> obtenerLibros() {
 // 1. Abrimos la sesión (usamos try-with-resources para que se cierre sola)
 try (Session session = HibernateUtil.getSessionFactory().openSession()) {
 
 // 2. Creamos la consulta HQL
 // ¡IMPORTANTE! Ponemos "Libros" (la Clase), no "libros" (la tabla)
 Query<Libros> consulta = session.createQuery("from Libros", Libros.class);
 
 // 3. Devolvemos la lista de objetos
 return consulta.list();
 
 } catch (Exception e) {
 System.err.println("Error: " + e.getMessage());
 return null;
 }
 }
}
```

---

## 💡 Los 3 trucos para no fallar en el DAO:

1. **HQL vs SQL:** En el DAO de Hibernate, si tu clase se llama `Libros` con **L mayúscula**, en la consulta tienes que poner `from Libros`. Si pones el nombre de la tabla de la base de datos, te dará error.
 
2. **El try-with-resources:** Fíjate que en el ejemplo ponemos `try (Session session =...)`. Esto es vital para que la sesión se cierre siempre, aunque algo falle. Si no lo haces, dejarás conexiones abiertas y el servidor petará.
 
3. **Separación total:** En el `Main` de tu programa (el `App.java`), nunca verás código de Hibernate. Solo verás: `dao.obtenerLibros();`. Así el código queda limpísimo.