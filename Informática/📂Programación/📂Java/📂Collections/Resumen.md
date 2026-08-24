
| Colección | Permite duplicados                     | Orden            | Acceso        |
| --------- | -------------------------------------- | ---------------- | ------------- |
| List      | Sí                                     | Sí               | Por índice    |
| Set       | No                                     | Depende del tipo | No por índice |
| Map       | Clave única, valor duplicado permitido | Depende del tipo | Por clave     |

|Colección|Duplicados|Orden|Acceso|Ejemplo|
|---|---|---|---|---|
|ArrayList|Sí|Sí (inserción)|Por índice|List|
|LinkedList|Sí|Sí (inserción)|Por posición (lento)|List|
|HashSet|No|No|No por índice|Set|
|TreeSet|No|Sí (orden natural o Comparator)|No por índice|Set|
|HashMap|Claves únicas|No|Por clave|Map|
|TreeMap|Claves únicas|Sí (orden natural o Comparator)|Por clave|Map|