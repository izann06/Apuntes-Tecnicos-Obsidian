El **ViewModel** es la capa que sobrevive a los cambios de configuración (como girar la pantalla) y gestiona la lógica de la interfaz de usuario.

## 1. Los 3 Pilares del Estado

Para que una app sea profesional, el ViewModel debe informar a la UI de tres cosas mediante `StateFlow`:

1. **`posts`**: La lista de datos (lo que queremos mostrar).
 
2. **`loading`**: Un booleano. Si es `true`, la UI muestra una rueda de carga.
 
3. **`error`**: Un mensaje de texto. Si no es `null`, la UI muestra el error.
 

---

## 2. El Código (MainViewModel.kt)

![[Pasted image 20260114000131.png]]

---

## 3. Conceptos Clave para entender el código

### A. `viewModelScope.launch`

Las llamadas a internet son **asíncronas**. No podemos hacerlas en el "hilo principal" porque la app se congelaría. Esta función abre un "hilo secundario" que se cierra automáticamente si el usuario sale de la pantalla, evitando fugas de memoria.

### B. `MutableStateFlow` vs `StateFlow`

- **`_posts` (Mutable):** Solo el ViewModel puede cambiar los datos (es la parte "privada" del estado).
 
- **`posts` (Público):** La UI solo puede "escuchar" o leer. No puede modificar la lista directamente. Esto se llama **encapsulamiento**.
 

### C. El bloque `finally`

Es muy importante. El código dentro de `finally` se ejecuta **siempre**, tanto si el `try` funcionó como si saltó el `catch`. Lo usamos para poner `loading = false`, asegurándonos de que la rueda de carga desaparezca pase lo que pase.

---

## 4. Flujo de datos en el ViewModel `fecthPosts()`

1. **Inicio:** `loading = true`, `error = null`.
 
2. **Llamada:** Se pide `repository.getPosts()`.
 
3. **Resultado A (Éxito):** Se actualiza `_posts` con los datos.
 
4. **Resultado B (Fallo):** Se actualiza `_error` con el mensaje.
 
5. **Fin:** `loading = false`.