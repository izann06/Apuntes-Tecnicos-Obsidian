Para que la aplicación no se quede congelada y el usuario sepa qué está pasando, usamos una **Sealed Class** (`LoginState`). Es como un semáforo:

- **`Idle`**: El estado inicial. No está pasando nada, el usuario está mirando la pantalla.
 
- **`Loading`**: Hemos pulsado el botón y estamos esperando al servidor. Aquí pondríamos el circulito de carga.
 
- **`Success`**: ¡Éxito! Tenemos la respuesta del servidor. Recibe un objeto `LoginResponse`.
 
- **`Error`**: Algo falló (sin internet, datos mal...). Recibe un mensaje para mostrarlo en un Toast o SnackBar.

```Kotlin
sealed class LoginState { 
	// Estado inactivo (esperando acción del usuario) 
 object Idle : LoginState()
 // Estado cargando (esperando respuesta del servidor)
 object Loading : LoginState()
 // Estado éxito (respuesta correcta del servidor)
 data class Success(val response: LoginResponse) : LoginState()
 // Estado error (respuesta incorrecta del servidor) 
 data class Error(val message: String) : LoginState() 
}
```