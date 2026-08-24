Aquí definimos el **contrato** con el backend usando la interfaz `ApiService`.

- **`@POST("login")`**: Enviamos el `LoginRequest`. Es la única ruta que **no** necesita token (porque precisamente vamos a por él).
![[04-Comunicación con Servidor(Retrofit)-1.png]]
    
- **`@Header("Authorization")`**: Para todas las demás peticiones, el servidor nos exige la "llave".
 ![[04-Comunicación con Servidor(Retrofit).png]]
    
- **`@Path` vs `@Body`**:
    
    - `@Path`: Sustituye una parte de la URL (ej: `{id}`).
        
    - `@Body`: Envía un objeto completo convertido a JSON.

Ejemplo:

```Kotlin
//Login  
@POST("login")  
@Headers("Content-Type: application/json") // Indica que el contenido es JSON.  
suspend fun postLogin(@Body request: LoginRequest): Response<LoginResponse>  
  
//Lista de cafes  
@GET("coffee")  
suspend fun getCoffees(@Header("Authorization") token: String): List<Coffee>  
  
//Obtener un cafe por su id  
@GET("coffee/{id}")  
suspend fun getCoffeeById(  
    @Header("Authorization") token: String,  
    @Path("id") id: Int): Response<Coffee>
```