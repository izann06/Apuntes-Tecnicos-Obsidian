
# 🔥 **Firewall (Cortafuegos)**

Un **firewall** es como **el portero de una discoteca** 🚷  
Decide quién entra y quién no.

👉 Ejemplo:  
Tu ordenador recibe miles de conexiones cada segundo.  
El firewall revisa:

- De dónde vienen
    
- Qué quieren hacer
    
- Y si son seguras o no
    

🔹 Si alguien intenta colarse (por ejemplo, un virus o hacker),  
el firewall lo **bloquea**.

🔹 Si una app necesita Internet (por ejemplo, Steam o Chrome),  
el firewall **le da permiso**.

➡️ En resumen:

> El firewall **protege tu ordenador** controlando qué entra y qué sale de la red.

🧠 Extra:  
En redes grandes (como una empresa) hay **firewalls físicos** (cajas especiales)  
que protegen **toda la red**, no solo un PC.

---


# 💉 **Inyecciones (SQL Injection)**

Una **inyección SQL** ocurre cuando alguien mete código malicioso en un formulario o campo de texto que se conecta directamente a la base de datos.

**Ejemplo:**  
Formulario de login:

![[Definiciones-7.png]]

Si no se valida bien, alguien podría escribir:

![[Definiciones-8.png]]

Y la consulta se vuelve:

![[Definiciones-9.png]]

➡ “1=1” siempre es verdad, así que el hacker entra sin contraseña.

**Cómo evitarlo:**

- Usar consultas preparadas.
    
- Validar la entrada del usuario.
    
- No concatenar texto directamente en SQL.

-------------------------------------------------

# 🔐 **SHA256 y los hashes**

SHA256 es un **algoritmo hash**, es decir, convierte un texto en una cadena larga de números y letras (64 caracteres).  
👉 Siempre devuelve el **mismo resultado para el mismo texto**, pero **no se puede volver atrás**.

**Ejemplo:**

`Entrada: hola 

`Salida: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824`

Si escribes “hola” **siempre dará esa misma cadena**.  
Pero si cambias una sola letra (“Hola”), el resultado es completamente diferente.

**Uso real:**

- Guardar contraseñas sin mostrar el texto real.
    
- Comprobar si un archivo fue modificado.
    

-------------------------------------------------

# **Cifrado**

Transformar información para que solo quien tenga la clave pueda leerla.

**Ejemplo real:**

- WhatsApp cifra tus mensajes para que solo tú y el receptor los puedan leer.


--------------------------------------------------------------------
