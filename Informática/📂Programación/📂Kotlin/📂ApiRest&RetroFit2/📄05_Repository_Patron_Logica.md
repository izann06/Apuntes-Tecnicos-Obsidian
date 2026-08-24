En esta fase, el Repositorio actúa como un **intermediario simple**. Su trabajo es intentar traer los datos de la nube y asegurarse de que la aplicación no se cierre (crash) si algo sale mal.

> [!NOTE] Diferencia con la versión Offline
> 
> Aquí solo inyectamos RemoteDatasource. No hay base de datos local (LocalDatasource). Si no hay internet, no hay datos que mostrar.`IMPORTANTE, MAS ADELANTE SI SE IMPLEMENTA EN REPOSITORY LOCALDATASOURCE CON ROOM.`

## 1. El Código Ejemplo

![[Pasted image 20260113235227.png]]

---

## 2. Explicación de la Lógica (Paso a Paso)

Este código maneja **tres escenarios posibles**:

### A. Escenario Ideal (Éxito) 🟢

1. Llamamos a `remoteDatasource.getPosts()` que lo guardamos en una variable.
    
2. Si `response.isSuccessful` es `true`.
    
3. Todo ha ido bien, entonces`response.body()` tiene los datos.
    
4. El Repositorio entrega la lista limpia al ViewModel.
    

### B. Escenario "Error del Servidor" (400-500) 🟠

- **¿Qué pasa?** Tienes internet, llegas al servidor, pero el servidor te dice "No encontrado" (404) o "Error interno" (500).
    
- **La decisión:** `response.isSuccessful` es `false`.
    
- **La acción:** Logueamos el error y devolvemos `emptyList()`.
    
- **¿Por qué?** Porque la conexión funcionó. Simplemente no hay posts. La app muestra una lista vacía, no un error rojo.
    

### C. Escenario "Excepción" (Sin Conexión) 🔴

- **¿Qué pasa?** No tienes WiFi, estás en modo avión o la URL está mal escrita.
    
- **La decisión:** Salta el bloque `catch (e: Exception)`.
    
- **La acción:** `throw e`.
    
- **¿Por qué lanzamos el error?**
    
    - Como **no tenemos base de datos (ROOM)** de respaldo, no tenemos nada que enseñar.
        
    - Al hacer `throw e`, obligamos al **ViewModel** a enterarse de que hubo un error grave para que pueda mostrar un mensaje al usuario (ej: un `Toast` o un texto rojo diciendo "Sin conexión").
        

---

### Esto es clave

- Si en este código tuviéramos Room y por ende el localDatasource, si falla internet, **no se lanza una excepción**, sino que devolvemos los datos guardados de la BD.
    
- En este código (sin ROOM), si falla internet, **tenemos que lanzar la excepción (`throw`)** porque es la única forma de decirle a la pantalla: "Oye, ha pasado algo malo y no tengo datos".