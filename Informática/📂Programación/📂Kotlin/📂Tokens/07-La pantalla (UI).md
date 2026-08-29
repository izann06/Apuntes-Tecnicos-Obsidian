Aquí es donde el usuario ve el resultado de todo el trabajo anterior. Usamos un `when(loginState)` para decidir qué mostrar:

- **`LaunchedEffect`**: Se lanza nada más abrir la pantalla para comprobar si ya estábamos logueados (`getSessionFlow`).
 
- **Estados visuales**:
 
 - `Loading`: Mostramos el componente `Loading()`.
 
 - `Success`: Usamos el `navController` para saltar a la lista de cafés.
 
 - `Idle`: Mostramos el diálogo para escribir usuario y pass.
 
 - `Error:` Muestra error.