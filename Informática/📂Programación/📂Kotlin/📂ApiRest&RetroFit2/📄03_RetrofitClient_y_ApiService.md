Este archivo contiene dos piezas fundamentales que trabajan juntas:

1. **ApiService (La Carta del Menú):** Define qué podemos pedirle al servidor.

2. **RetrofitClient (El Camarero):** Configura cómo se hace el pedido y cómo se conecta.

---

## 1. La Interfaz (ApiService)

En Kotlin, una `interface` es un contrato. Aquí no escribimos código lógico, solo definimos las reglas de las peticiones.Es como el DAO,pero en este caso de la API.

![[Pasted image 20260113233531.png]]

### Desglose línea a línea:

- **`@GET("posts")`**:
    
    - Indica que usaremos el verbo HTTP **GET** (leer datos).
        
    - **"posts"** es el _endpoint_. Se pegará al final de la URL base.
        
- **`suspend`**:
    
    - Palabra clave de **Corutinas**. OBLIGATORIA para que la petición se haga en segundo plano y no congele la app.
        
- **`Response<...>`**:
    
    - Es el envoltorio de Retrofit. Dentro vendrá:
        
        - El código de estado (ej. 200, 404).
            
        - El cuerpo (`body`) con los datos.
            
        - Los mensajes de error si los hay.
            
- **`@Path("id")`**:
    
    - Se usa para URLs dinámicas. Sustituye la parte `{id}` de la URL por el valor de la variable `id` (Entero).
        

---

## 2. El Cliente Singleton (RetrofitClient)

Necesitamos configurar Retrofit. Como es un proceso pesado (consume recursos), utilizamos un `object` para asegurar que **solo exista una instancia** en toda la aplicación (Patrón Singleton).

Esto se debe a que no queremos crear 100 conexiones a internet, queremos una sola en toda la app y reutilizarla.



![[Pasted image 20260113233517.png]]

### Desglose de la configuración:

- **`object`**: Convierte la clase en un Singleton estático. Se puede acceder desde cualquier sitio escribiendo `RetrofitClient.apiService`.
    
- **`by lazy`**: Esto es muy eficiente. Significa que la conexión no se crea en cuanto abres la app, sino **solo la primera vez que la necesites**.
    
- **`Retrofit.Builder()`**: Es el constructor. Aquí empezamos a configurar el "camión" que traerá los datos.
    
- **`.baseUrl(BASE_URL)`**: Le decimos a dónde tiene que ir.
    
- **`.addConverterFactory(GsonConverterFactory.create())`**: Esta línea es vital. Le estás instalando el **traductor**. Le dices: "Cuando descargues el texto JSON, usa la librería **GSON** para convertirlo automáticamente en mis clases `Post` de Kotlin". Sin esto, recibirías texto plano y tendrías que trocearlo tú a mano.
    
- **`.build()`**: Cierra la configuración y crea el objeto Retrofit.
    
- **`.create(ApiService::class.java)`**: Aquí es donde ocurre la unión. Retrofit coge tu **interfaz** (que solo tiene nombres de funciones) y genera el código real que hace las llamadas a internet.
        

---

## 3. Resumen visual del funcionamiento

Cuando llamas a `getPostById(5)`, ocurre esta fusión:

|**Componente**|**Valor**|
|---|---|
|**Base URL** (RetrofitClient)|`https://jsonplaceholder.typicode.com/`|
|**Endpoint** (ApiService)|`posts/`|
|**Path** (Parámetro)|`5`|
|**Resultado Final**|`https://jsonplaceholder.typicode.com/posts/5`|