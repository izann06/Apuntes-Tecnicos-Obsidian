Antes de indagar en esta clase debemos entender que es `datastore`.

Datastore sirve para guardar datos de forma local en el dispositivo.

- **¿Para qué sirve?** Para guardar pequeñas cantidades de información que deben sobrevivir aunque la app se cierre o el móvil se reinicie (como un **Token de sesión**, el nombre de usuario o ajustes de modo oscuro).
    
- **¿Por qué es mejor?** * **Seguridad:** Se ejecuta fuera del hilo principal (UI thread), por lo que nunca "congela" la pantalla.
    
    - **Reactividad:** Utiliza **Flows**, lo que significa que la app "escucha" los cambios en tiempo real. Si borras el token, la app se entera al instante.

Ahora vamos con la clase de `SessionManager`:

Esta clase es el "cerebro" que decide cómo se guarda y se recupera la sesión del usuario.

### A. Las llaves (Keys)

Para guardar algo en DataStore, necesitamos una etiqueta única.



```Kotlin
private val TOKEN_KEY = stringPreferencesKey("token")
private val USERNAME_KEY = stringPreferencesKey("username")
```

> **Nota:** Es como ponerle una pegatina a un cajón. Si quieres el token, buscas la pegatina `"token"`.

---

### B. El Flujo de Sesión (`sessionFlow`)

Este es el punto más importante de tu código:



```Kotlin
val sessionFlow: Flow<Pair<String?, String?>> = dataStore.data.map { preferences ->
    preferences[TOKEN_KEY] to preferences[USERNAME_KEY]
}
```

- **¿Qué hace?**: Crea un flujo constante de datos.
    
- **El `Pair`**: En lugar de devolver una sola cosa, devolvemos un "pack" de dos: `(token, username)`.
    
- **Reactividad**: Si el token cambia en cualquier parte de la app, cualquier pantalla que esté escuchando este `sessionFlow` se actualizará automáticamente. Es como un grifo que siempre tiene agua fresca.
    

---

### C. Guardar Sesión (`saveSession`)

Cuando el servidor nos dice que el login es correcto, llamamos a esta función:

```Kotlin
suspend fun saveSession(token: String, username: String) {
    dataStore.edit { preferences -> 
        preferences[TOKEN_KEY] = token
        preferences[USERNAME_KEY] = username
    }
}
```

- **`suspend`**: Obligatorio. Escribir en la memoria del móvil lleva tiempo (milisegundos), así que Kotlin suspende la función para no congelar la app.
    
- **`edit`**: Es una transacción segura. O se guardan los dos datos correctamente, o no se guarda ninguno.
    

---

### D. Borrar Sesión (`clearSession`)

El botón de "Cerrar sesión" llamará a esto:



```Kotlin
suspend fun clearSession() {
    dataStore.edit { 
        it.remove(TOKEN_KEY)
        it.remove(USERNAME_KEY)
    }
}
```

Al eliminar las llaves, el `sessionFlow` que explicamos antes emitirá automáticamente un par de valores `null`. Esto provocará que la app sepa que ya no hay nadie logueado.

---

## 💡 Resumen para el ViewModel

Cuando uses esto en tu `ViewModel`, recuerda que `it.first` será el **Token** e `it.second` será el **Username**.

> [!IMPORTANT] **¿Por qué usamos `!!` en el ViewModel?** 
> En el código hay que poner `username = it.second!!`. Esto le dice a Kotlin: Estoy 100% seguro de que si hay un token, también hay un nombre de usuario. Ten cuidado, porque si por algún error el nombre no se guardó, la app podría petar (crash). ¡Asegúrate siempre de guardar ambos a la vez en `saveSession`!