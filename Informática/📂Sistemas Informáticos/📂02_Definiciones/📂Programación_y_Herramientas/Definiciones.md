# ⚙️ **API (Interfaz de Programación de Aplicaciones)**

Piensa en una **API** como **un camarero en un restaurante** 🍽️

- Tú (el cliente o app) no entras a la cocina (el servidor o base de datos).
    
- En su lugar, le **pides al camarero (API)** lo que quieres:
    
    > “Quiero una pizza margarita.”
    
- El camarero va a la cocina, lo pide al cocinero y te trae la pizza lista.
    

👉 En el mundo real:

- Tú usas una **app del tiempo**.
    
- Esa app **no tiene los datos del clima**, se los pide a una **API de meteorología**.
    
- La API responde con datos en formato fácil (por ejemplo, JSON):
    
    `{   "ciudad": "Madrid",   "temperatura": 18,   "estado": "Soleado" }`
    
- La app lo muestra bonito en pantalla ☀️
    

➡️ En resumen:

> Una API es un **mensajero o camarero** que conecta dos programas para que se entiendan.

🧠 Extra:  
Muchas webs tienen APIs públicas. Por ejemplo, la de Pokémon:  
`https://pokeapi.co/`  
Puedes pedir información sobre cualquier Pokémon.

---

# 🧩 **Framework**

Un **framework** es como un **esqueleto ya armado** para construir más rápido.  
Te da la **estructura básica** para no empezar desde cero.

👉 Ejemplo fácil:  
Piensa en un **LEGO con instrucciones**.  
El framework te da la base y las piezas necesarias para construir una casa,  
y tú solo te preocupas de **decorar** o **añadir funciones**.

👉 Ejemplo real:

- **Django (Python)** → te da una estructura para hacer páginas web.
    
- **Spring (Java)** → te da herramientas para manejar datos, servidores y seguridad.
    
- **React (JavaScript)** → te ayuda a crear páginas web dinámicas.
    

➡️ En resumen:

> Un framework **organiza y acelera** el trabajo de un programador.  
> Tú solo “rellenas” con tus propias funciones.

---

# 📚 **Librería (Library)**

Una **librería** es como **una caja de herramientas** 🔧  
No te da la estructura de la casa (como el framework),  
sino **bloques o funciones que puedes usar donde quieras**.

👉 Ejemplo fácil:

- Si quieres construir una casa (programa),  
    una librería sería un **martillo**, **taladro**, o **ventanas ya hechas**.
    
- Tú decides **cómo y cuándo usarlas**.
    

👉 Ejemplo real:

- **NumPy (Python)** → tiene funciones matemáticas listas.
    
- **Lombok (Java)** → te ahorra escribir código repetido.
    
- **Axios (JavaScript)** → sirve para hacer peticiones a APIs fácilmente.
    

➡️ En resumen:

> Una librería **no impone reglas**, solo te da **herramientas útiles**.  
> Un framework **te da la estructura completa**.

📖 Diferencia visual:

|Tipo|Qué da|Ejemplo|
|---|---|---|
|Librería|Herramientas sueltas|Axios, NumPy|
|Framework|Estructura + reglas|React, Spring|

---

# ⚙️  **CI/CD (Integración y Despliegue Continuos)**

Esto es **automatización del trabajo de programadores**.  
Sirve para que los programas se **actualicen solos sin errores**.

👉 Ejemplo fácil:  
Piensa en un **cocinero robot** en una cocina 🍳  
Cada vez que alguien sube una receta nueva:

1. El robot **prueba la receta (CI)** → ve si hay errores.
    
2. Si todo está bien, **sirve el plato al público (CD)** → publica la app automáticamente.
    

---

### 🧩 CI – _Integración Continua_

Cada vez que un programador cambia el código:

- El sistema lo **comprueba automáticamente** (busca errores, ejecuta pruebas).
    
- Si todo pasa bien → sigue.
    
- Si algo falla → avisa al programador.
    

Ejemplo:  
Subes código a GitHub → GitHub Actions lo prueba automáticamente.

---

### 🚀 CD – _Despliegue Continuo_

Si el código está bien:

- El sistema **lo sube automáticamente al servidor o la web**.  
    Ya no hace falta que alguien lo haga manualmente.
    

Ejemplo:  
Subes un cambio → tu web en Internet se actualiza sola.

➡️ En resumen:

| Parte | Significa            | Qué hace                   | Ejemplo          |     |
| ----- | -------------------- | -------------------------- | ---------------- | --- |
| CI    | Integración continua | Prueba el código           | GitHub Actions   |     |
| CD    | Despliegue continuo  | Lo publica automáticamente | Netlify, Jenkins |     |

-------------------------------------------------


# ✍️ ¿Qué es un Editor o IDE?

Es el **programa donde escribes código**.

👉 Ejemplo:

- **VS Code** → muy popular para casi todos los lenguajes.(Editor)
    
- **IntelliJ IDEA** → muy usado para Java.(IDE)
    
- **PyCharm** → para Python.
    

La diferencia es que un **editor** solo sirve para escribir texto,  
mientras que un **IDE** (entorno de desarrollo) incluye cosas como:

- Botón de ejecutar
    
- Depurador (para ver errores)
    
- Sugerencias automáticas

-------------------------------------------------


# 🔁 ¿Qué es REST?

**REST** (Representational State Transfer) es un **estilo arquitectónico** para construir APIs que usan HTTP. No es un protocolo, sino un conjunto de reglas/convenciones para que clientes y servidores se comuniquen de forma simple, escalable y uniforme. Fue definido por Roy Fielding en su tesis (2000). 

## Principios y características clave (con ejemplos)

1. **Recursos identificados por URIs**
    
    - Un recurso es una “cosa” (usuarios, productos).
        
    - Ejemplo: `GET /usuarios/123` → obtiene los datos del usuario 123.
        
2. **Uso de métodos HTTP semánticos**
    
    - `GET` (leer), `POST` (crear), `PUT` (Actualizar), `DELETE` (borrar).
        
    - **Ejemplo de flujo**:
        
        - `POST /productos` con JSON crea un producto.
            
        - `GET /productos/55` devuelve ese producto.
            
        - `PUT /productos/55` sobrescribe los datos.
            
        - `DELETE /productos/55` lo borra.
            
3. **Sin estado (stateless)**
    
    - Cada petición contiene toda la información necesaria (el servidor no guarda la sesión entre peticiones).
        
    - Ventaja: escalabilidad.
        
4. **Representaciones (JSON, XML)**
    
    - El recurso puede representarse en varios formatos; JSON es el más común.
        
    - **Content negotiation:** cliente pide `Accept: application/json` y servidor responde JSON.
        
5. **HATEOAS (opcional en muchos sistemas)**
    
    - El servidor devuelve enlaces dentro de la respuesta para indicar acciones disponibles sobre el recurso (menos usado en APIs simples, pero forma parte del estilo REST purista).
        
6. **Idempotencia**
    
    - `GET`, `PUT`, `DELETE` deben ser idempotentes: ejecutarlos varias veces produce el mismo resultado. `POST` no lo es (crea recursos nuevos).
        
7. **Códigos HTTP**
    
    - `200 OK`, `201 Created` (cuando un recurso se crea), `204 No Content` (operación correcta sin cuerpo), `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `500 Internal Server Error`.
        

## Ejemplo completo (mini-escenario)

- **Crear usuario:**  
    `POST /usuarios`  
    Body JSON: `{ "nombre": "Izan", "email": "a@b.com" }`  
    Respuesta: `201 Created`, body con `{ "id": 123, "nombre": ... }`.
    
- **Obtener usuario:**  
    `GET /usuarios/123` → `200 OK` + JSON con los datos.
    

---

## Por qué REST es importante en clase y en todos los lenguajes

REST define **convenciones universales** (URIs, métodos HTTP, códigos) que cualquier lenguaje puede implementar (Python, Java, JavaScript, Go…). Eso es lo que dijo tu profe: **conectar sistemas → usar HTTP+REST + JSON** es lo más común porque es simple, interoperable y soportado por todo.

-------------------------------------------------

# **Overclock**

Aumentar la velocidad del procesador más allá de lo normal, para mejorar rendimiento.

**Ejemplo real:**

- Jugar videojuegos pesados más rápido aumentando la frecuencia del CPU, pero cuidado: puede calentar demasiado el ordenador.
    

---

# **OpenWebinars o Udemy**

Plataforma online para aprender tecnología y desarrollo. 

**Ejemplo real:** Tomar un curso de Docker o Python desde casa.

-------------------------------------------------

# **Medium**

Plataforma de blogs donde profesionales publican artículos técnicos. 

**Ejemplo real:** Aprender buenas prácticas de programación leyendo posts de desarrolladores expertos.

-------------------------------------------------

# **Principios SOLID**

Los **principios SOLID** son **5 reglas** para escribir código **ordenado, fácil de mantener y sin errores raros** cuando el proyecto crece.  
Piensa en ellos como las “normas de higiene del código”.

### 1️⃣ **S — Single Responsibility (Responsabilidad Única)**

👉 Cada clase o función debe hacer **solo una cosa**.

**Ejemplo malo:**

![[Definiciones.png]]
**Ejemplo bueno:**

![[Definiciones-1.png]]

➡ Así si mañana cambias la forma de enviar correos, no tocas el código del usuario.

---

### 2️⃣ **O — Open/Closed (Abierto a extensión, cerrado a modificación)**

👉 Puedes **añadir nuevas funciones** sin tener que cambiar las viejas.

**Ejemplo real:**  
Tienes una clase que calcula descuentos.  
Mañana quieres añadir un nuevo tipo de descuento sin romper lo anterior.

**Ejemplo:**

![[Definiciones-2.png]]

➡ Puedes crear más tipos de descuento sin tocar las clases ya hechas.

---

### 3️⃣ **L — Liskov Substitution (Sustitución de Liskov)**

👉 Si una clase hereda de otra, debe **poder usarse igual** que la original, sin romper nada.

**Ejemplo real:**  
Si tienes una clase `Animal` y otra `Perro extends Animal`, cualquier función que use un `Animal` debería poder aceptar un `Perro` sin problema.

![[Definiciones-3.png]]

➡ Si metes un `Perro` donde antes había un `Animal`, el programa sigue funcionando.

---

### 4️⃣ **I — Interface Segregation (Segregación de Interfaces)**

👉 No obligues a una clase a tener métodos que **no necesita**.

**Ejemplo malo:**

![[Definiciones-4.png]]

**Ejemplo bueno:**

![[Definiciones-5.png]]

➡ Cada uno tiene lo que necesita, nada más.

---

### 5️⃣ **D — Dependency Inversion (Inversión de Dependencias)**

👉 Las clases deben depender de **abstracciones (interfaces)**, no de implementaciones concretas.

**Ejemplo real:**  
Una clase `Factura` necesita enviar un correo.  
En vez de depender directamente de `CorreoService`, depende de una interfaz `Notificador`.

![[Definiciones-6.png]]

➡ Así puedes cambiar la forma de enviar notificaciones sin tocar `Factura`.


--------------------------------------------------------------------


#  **Serializar**

Es **convertir un objeto en un formato que se pueda guardar o transmitir** (por ejemplo, a un archivo o a través de una red).  
Ese formato suele ser **texto** (como JSON, XML) o **binario**.

👉 En pocas palabras:

> “Serializar es transformar un objeto en datos (texto o bytes)”.

📦 Ejemplo en JSON (muy común en APIs):

`Persona p = new Persona("Izan", 21); String json = gson.toJson(p);`

Resultado:

`{"nombre":"Izan","edad":21}`

---

# **Deserializar**

Es **el proceso inverso**: tomar esos datos (por ejemplo el JSON anterior) y **reconstruir el objeto original** en memoria.

👉 En pocas palabras:

> “Deserializar es pasar de datos a objeto”.

Ejemplo:

`Persona p = gson.fromJson("{\"nombre\":\"Izan\",\"edad\":21}", Persona.class);`