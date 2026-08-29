El **ViewModel** es el intermediario. Su responsabilidad es conectar la UI con el Repositorio, manejando el ciclo de vida y los hilos de ejecución (Corrutinas).

## 1. Configuración Inicial (`AndroidViewModel`)

A diferencia de un ViewModel normal, aquí heredamos de **`AndroidViewModel`**.

- **¿Por qué?** Porque necesitamos el `Application` (Contexto) para construir la base de datos con `AppDatabase.getInstance(application)`.
 


![[Pasted image 20260114140939.png]]


---

## 2. Gestión de Flows (`collect`)

Los `Flows` son "tuberías" frías. Si nadie abre el grifo (`collect`), el agua no sale. Por eso lanzamos corrutinas en el `init` para empezar a escuchar los cambios de la BD y actualizar nuestros `StateFlows`.

![[Pasted image 20260114141006.png]]

---

## 3. Operaciones Asíncronas con Retorno (`Deferred`)

A veces necesitamos guardar algo y **esperar** a saber si se ha guardado bien o cuál fue el resultado (ej: cuántas filas se borraron), pero sin bloquear la UI.

Para esto usamos **`async`** y **`Deferred`**.

- `launch`: "Lanza y olvida" (Fire and forget).
 
- `async`: "Lanza y devuélveme una promesa de resultado futuro" (`Deferred`).
 

![[Pasted image 20260114141102.png]]

> [!NOTE] Diferencia `launch` vs `async`
> 
> - Usa **`launch`** cuando no te importe qué devuelve la función (ej: guardar un log).
> 
> - Usa **`async`** cuando necesites el dato de vuelta para seguir trabajando (ej: buscar un usuario por ID y luego mostrar su nombre).
> 

---

## 4. Consultas Puntuales (`getById`)

Si queremos buscar un solo dato, también usamos `async` porque la operación puede tardar unos milisegundos y no queremos congelar la pantalla.

![[Pasted image 20260114141038.png]]