Vamos a poner de modelo a `Post` por ejemplo:

El Modelo es una clase de datos (`data class`) que sirve de **espejo** para el JSON que viene del servidor. Su única función es almacenar información; no tiene lógica ni cálculos.

## 1. Comparativa JSON vs Kotlin

Imagina que el servidor te envía este paquete (JSON). Para que Android lo entienda, necesitamos crear un molde exacto en Kotlin.

|**JSON (Lo que recibes)**|**Kotlin (Tu molde)**|
|---|---|
|`{`|`data class Post(`|
|`"userId": 1,`|`val userId: Int,`|
|`"id": 1,`|`val id: Int,`|
|`"title": "hola...",`|`val title: String,`|
|`"body": "texto..."`|`val body: String`|
|`}`|`)`|

---

## 2. Código: Versión Básica (Solo Retrofit)

Si solo vamos a leer de internet y mostrar en pantalla, esta es la estructura. Se guarda dentro del paquete `data/model`.

![[Pasted image 20260113232210.png]]

---

## 3. Código: Versión Avanzada (Retrofit + ROOM)

Como el objetivo del tema es guardar los datos en local (caché offline), debemos asignar a nuestra clase con anotaciones de ROOM. Así, la misma clase sirve para leer de internet y para ser una tabla en la base de datos.


![[Pasted image 20260114001931.png]]

> [!WARNING] Regla de Oro de los Nombres
> 
> Los nombres de las variables (userId, title) deben ser idénticos a los del JSON.
> 
> - Si en el JSON dice `"user_id"` y tú pones `val userId`, **no funcionará** (saldrá null o 0).
> 
> - Solución: Si quieres poner un nombre distinto en el atributo de la data class para que el JSON sepa a que articulo está asociado, debes usar la anotación @SerializedName on el atributo del JSON

---

## 4.Plugin "JSON To Kotlin Class"

Cuando el JSON es enorme y tiene 50 campos, escribirlos a mano es una pérdida de tiempo y dolor de cabeza. Android Studio tiene un plugin para hacerlo automático:

1. Copia el texto JSON crudo (desde el navegador).
 
2. En Android Studio: Clic derecho en la carpeta `model` -> `New` -> `Kotlin Data Class File from JSON`.
 
3. Pega el JSON y dale un nombre.
 
4. Hay un boton que es **Advanced** dentro vete a **Annotation** y selecciona Gson. Acepta.
 

---

¿Todo claro con el modelo? Fíjate que en la versión de ROOM he puesto `autoGenerate = false` en la PrimaryKey. **¿Sabes por qué?** Porque el ID ya nos lo da el servidor (1, 2, 3...) y queremos respetar ese orden, no inventarnos IDs nuevos.