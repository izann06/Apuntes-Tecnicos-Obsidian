El `LoginViewModel` coordina todo. Tiene dos misiones principales:

1. **Hacer Login**: Llama al repositorio, espera el token y, **muy importante**, lo guarda en el `SessionManager` antes de decir que todo ha ido bien (`Success`).
 
2. **Auto-Login (`getSessionFlow`)**: Esta es la magia. Al arrancar, mira si hay algo en el DataStore. Si hay un token, salta directamente a la pantalla de éxito sin preguntar al usuario.
 

> [!WARNING] Fíjate que en `getSessionFlow` reconstruimos un `LoginResponse` falso con `ok = true`. Lo hacemos para "engañar" al estado de la UI y que crea que acabamos de recibir una respuesta positiva del servidor.

```Kotlin
//Login,nos dice el estado en el que se encuentra el login 
private val _loginState = MutableStateFlow<LoginState>(LoginState.Idle) 
val loginState: StateFlow<LoginState> = _loginState

init { 
 
	//Aqui va toda la parte de database,dao,local,remote y repository 
 
 val dataStore: DataStore<Preferences> = application.dataStore 
 sessionManager = SessionManager(dataStore) 
}
```

> [!WARNING] IMPORTANTE
> En el VIEWMODEL del Login debes poner el loginState para saber en que estado se encuentra el login.
> Pero en los demas VIEWMODEL no debes ponerlo simplemente dejamos el `datastore` y el `sessionManager`.