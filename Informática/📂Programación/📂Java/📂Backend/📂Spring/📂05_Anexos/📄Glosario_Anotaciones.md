# Diccionario de Anotaciones Spring 🏷️

| Anotación                | Capa / Uso | Explicación sencilla                            |
| :----------------------- | :--------- | :---------------------------------------------- |
| `@SpringBootApplication` | Main       | Arranca todo. Magia negra.                      |
| `@Entity`                | Modelo     | Esto es una tabla de SQL.                       |
| `@Id`                    | Modelo     | Clave primaria.                                 |
| `@GeneratedValue`        | Modelo     | Autoincremental (Serial).                       |
| `@Repository`            | Datos      | Habla con la BBDD (DAO vitaminado).             |
| `@Service`               | Servicio   | Aquí va la lógica de negocio.                   |
| `@RestController`        | Web        | Recibe peticiones HTTP y devuelve JSON.         |
| `@RequestMapping`        | Web        | Ruta base de la URL (ej. `/api/v1`).            |
| `@Autowired`             | General    | "Spring, búscame esto e inyéctalo aquí".        |
| `@PathVariable`          | Web        | Saca datos de la URL (`/usuarios/{id}`).        |
| `@RequestBody`           | Web        | Convierte el JSON que llega en un Objeto Java.  |
| `@JsonIgnore`            | Modelo     | ¡Cuidado! Evita bucles infinitos en relaciones. |

