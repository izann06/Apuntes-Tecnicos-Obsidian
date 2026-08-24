Esta es la versión definitiva del Repositorio. Su objetivo es garantizar que el usuario **siempre vea datos**, incluso si está en un túnel o en modo avión.

## 1. La Lógica: "Single Source of Truth" (Fuente Única de Verdad)

La estrategia cambia respecto a la versión anterior. Ahora no solo pasamos datos de un lado a otro, ahora **sincronizamos**.

1. **Prioridad:** Intentar descargar datos frescos de la Nube (API).
    
2. **Si hay éxito:** Guardarlos inmediatamente en la Caja Fuerte (ROOM) y luego entregarlos.
    
3. **Si hay fallo:** Abrir la Caja Fuerte y entregar lo que haya guardado de la última vez.
    

---

## 2. El Código (Repository.kt)

Ahora inyectamos **ambos** datasources en el constructor:
- RemoteDatasource
- LocalDatasource

![[Pasted image 20260114003053.png]]

---

## 3. Análisis detallado línea por línea

**Si ocurre el IF:**
### `localDatasource.insertAllPosts(posts)`

- **¿Qué hace?** Es el momento de la sincronización.
    
- **¿Por qué aquí?** Solo guardamos si la respuesta fue exitosa (`isSuccessful`). No queremos guardar basura o errores en nuestra base de datos limpia.


**Si ocurre el Else:**
### `localDatasource.getPosts().first()`

✔️ Se muestra el error HTTP  
✔️ Se devuelven los datos guardados en la base de datos local  
✔️ La app **no se rompe**
    

### En caso de que se vaya al bloque `catch (e: Exception)`

Aquí la lógica es:

1. Intenta usar la base de datos local
    
2. Si **hay datos**, se devuelven → la app sigue funcionando.
		Si el usuario ya abrió la app ayer, tendrá datos en caché -> **Se los mostramos** (aunque sean viejos). El usuario ni se entera de que no tiene internet.
    
3. Si **NO hay datos**, se relanza la excepción (`throw e`)
		Si es la primera vez que abre la app y encima no tiene internet -> **No tenemos nada**. Ahí sí lanzamos el error (`throw e`) para que el ViewModel muestre el mensaje rojo en pantalla.