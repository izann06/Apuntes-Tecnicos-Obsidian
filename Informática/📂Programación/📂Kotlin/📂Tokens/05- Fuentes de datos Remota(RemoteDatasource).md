El `RemoteDatasource` es el encargado de ensuciarse las manos con las respuestas del servidor.

- **El prefijo "Bearer"**: Es una regla estándar. No enviamos el token a secas, le ponemos delante la palabra `Bearer` (portador) para decirle al servidor: Eh, soy el portador de esta llave autorizada.
    
- **Gestión de Errores**: Usamos `response.isSuccessful`. Si falla, extraemos el `errorBody()` para saber si el error fue un 401 (no autorizado), un 500 (servidor roto), etc.
```Kotlin
// Función para obtener el login, se pasa el objeto RequestLogin en el body.  
// Se devuelve un objeto LoginResponse.  
suspend fun login(request: LoginRequest): LoginResponse {  
    val response = apiService.postLogin(request)  
    if (response.isSuccessful) {  
        return response.body() ?: throw Exception("Respuesta vacía del servidor")  
    } else {  
        val errorBody = response.errorBody()?.string() // Se obtienen detalles del error.  
        Log.e(TAG, "Error: ${response.message()} | $errorBody")  
        throw Exception("Error en login: ${response.message()}")  
    }  
}  
  
//Traer lista de cafes de la api  
suspend fun getCoffees(token: String) = apiService.getCoffees("Bearer $token")  

//Traer desde la api un cafe con un id asociado  
suspend fun getCoffeeById(token: String, id: Int) = apiService.getCoffeeById("Bearer $token",id) 

//Obtener comentarios de un cafe  
suspend fun getCommentsByCoffee(token: String, idCoffee: Int) = apiService.getCommentsByCoffee("Bearer $token",idCoffee)  

//Publicar un comentario  
suspend fun postComment(token: String, comment: Comment) = apiService.postComment("Bearer $token",comment)

```