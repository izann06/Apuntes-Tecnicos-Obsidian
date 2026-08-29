El **LocalDatasource** es el intermediario directo entre tu código y la Base de Datos ROOM. Su misión es aislar al Repositorio de la complejidad del DAO.

## 1. ¿Por qué necesitamos esta clase?

Al igual que creamos un `RemoteDatasource` para manejar Retrofit (la nube), creamos este para manejar ROOM (el disco).

Esto permite mantener una **simetría perfecta** en la arquitectura:

- **RemoteDatasource:** Habla con la API.
 
- **LocalDatasource:** Habla con la Base de Datos.
 
- **Repository:** Habla con los dos Datasources (no sabe ni de Retrofit ni de ROOM directamente).
 

---

## 2. El Código (LocalDatasource.kt)

![[Pasted image 20260114002645.png]]

---

## 3. Explicación Detallada

### La Función `getPosts()`

- Fíjate que devuelve `Flow<List<Post>>`.
 
- **Concepto Clave:** No estás pidiendo "dame los posts ahora". Estás diciendo: "Manténme informado de cualquier cambio en la tabla de posts".
 
- Si en otra parte de la app borras un post, este `Flow` avisará automáticamente y la pantalla se actualizará sola.
 

### La Función `insertAllPosts()`

- Recibe la lista que ha llegado de Internet.
 
- Llama al método del DAO que configuramos con `OnConflictStrategy.REPLACE`.
 
- **Resultado:** Si teníamos 10 posts viejos y llegan 10 nuevos con los mismos IDs, se borran los viejos y se quedan los nuevos. La caché se refresca.