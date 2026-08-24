Aqui se encuentran 2 clases:

**LoginRequest:** Es el paquete que nosotros enviamos.Contiene `User` y `Password`.

```Kotlin
data class LoginRequest(  
    @SerializedName("usuario")  
    val user: String,  
    @SerializedName("password")  
    val password: String  
)
```

### **Api:**
![[01-Modelos de Datos (DTOs).png]]

**LoginResponse:** Es el paquete que el servidor nos devuelve.Contiene `ok`, `token` `message`.

- `ok`: Un booleano para saber si fue bien.
    
- `token`: La llave que contiene nuestra información y usaremos en futuras peticiones, para no tener que iniciar sesión, sino que entraremos directamente.
    
- `message`: Un texto por si hay algún error (ej: "Contraseña incorrecta").

```Kotlin
data class LoginResponse(  
    @SerializedName("ok")  
    val ok: Boolean,  
    @SerializedName("token")  
    val token: String?,  
    @SerializedName("message")  
    val message: String?,  
    val username: String  
)
```

Hay dos posibles salidas que nos puede devolver la API.Correcto o Incorrecto.

Si es correcto,todo va bien pues nos responde con un HTTP 200:
![[01-Modelos de Datos (DTOs)-1.png]]

Si es incorrecto,hay algo mal ya puede ser credenciales,servidor...Hay muchos errores HTTP.
![[01-Modelos de Datos (DTOs)-2.png]]


Ahora bien,no he nombrado ninguna vez `username`,no es obligatorio usarlo,en la respuesta de la API ya vemos que no aparece pero si quieres usarlo sirve para esto.

##  ¿Qué cambia realmente en tu app?

| **Si dejas el username**                                                        | **Si quitas el username**                                      |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Puedes poner "Bienvenido, Izan" en la pantalla de inicio nada más abrir la app. | La app solo sabe que "alguien" ha entrado, pero no su nombre.  |
| Tienes que gestionar un dato más en el DataStore (un poco más de código).       | El código es más limpio y minimalista. Menos margen de error.  |
| Útil si el usuario puede cambiar de cuenta a menudo.                            | Solo te importa que el Token sea válido para hacer peticiones. |
