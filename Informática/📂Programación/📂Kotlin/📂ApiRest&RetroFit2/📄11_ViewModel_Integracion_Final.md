Este archivo sustituye al ViewModel básico que vimos al principio. Ahora, como tenemos base de datos, necesitamos un cambio importante: el **Contexto**.

## 1. El cambio a `AndroidViewModel`

- **Antes:** Usábamos `ViewModel()`.
    
- **Ahora:** Usamos `AndroidViewModel(application)`.
    
- **¿Por qué?** Para crear la base de datos ROOM (`AppDatabase.getInstance(context)`), necesitamos pasarle el `Context` (el entorno de la app). Un ViewModel normal no tiene acceso a ese contexto, pero el `AndroidViewModel` sí.
    

---

## 2. El Código (MainViewModel.kt) Ejemplo:

![[Pasted image 20260114004859.png]]

---

## 3. Explicación Detallada

Fíjate en el bloque `init`. Esto se llama **Inyección de Dependencias Manual**. Es como montar un mueble de IKEA paso a paso:

1. **Paso A (La Base):**
    
    - Pedimos la instancia de la base de datos (`AppDatabase`).
        
    - Sacamos la herramienta específica para Posts (`postsDAO`).
        
2. **Paso B (Las Piezas Intermedias):**
    
    - Creamos el `LocalDatasource` y le damos el DAO (para que pueda escribir en disco).
        
    - Creamos el `RemoteDatasource` (para que pueda llamar a la API).
        
3. **Paso C (El Ensamblaje Final):**
    
    - Creamos el `Repository` y le damos los dos datasources.
        
    - Ahora la variable `repository` está lista para usarse en el resto de la clase.
        

### ¿Por qué lo hacemos en el `init`?

Porque necesitamos que todo esto esté listo **antes** de que el usuario pulse ningún botón. En cuanto la pantalla se crea, el ViewModel se construye a sí mismo.