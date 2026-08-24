**Tags:** #aws #seguridad #nacl #security-groups #networking #cloud-practitioner #cp-redes

> [!summary] El Concepto Clave
> En AWS, la seguridad de red es como una cebolla: tiene capas. Para que un dato llegue a tu servidor, debe pasar primero por la frontera de la ciudad (ACL de Red) y luego por el portero del edificio (Grupo de Seguridad).

---

## 🎭 Las Analogías: Entendiendo el funcionamiento

### 1. La ACL de Red (NACL)

Es la seguridad a nivel de **Subred** (el barrio entero). 

* **Funcionamiento (Sin Estado / Stateless):** El guardia tiene memoria de pez.
   
    * **Entrada:** Mira si tu pasaporte está en la lista de permitidos. Si sí, pasas.
    * **Salida:** Cuando quieres irte, **no se acuerda de ti**. Tienes que volver a enseñarle los papeles y él debe verificar su lista de "salidas permitidas". Si no hay una regla de salida, te quedas atrapado.
      
* **Reglas:** Permite reglas de "Permitir" y "Denegar" (puedes crear una lista negra de IPs específicas).

### 2. El Grupo de Seguridad (Security Group)

Es la seguridad a nivel de **Instancia EC2** (tu servidor individual).

* **Funcionamiento (Con Estado / Stateful):** El portero tiene memoria fotográfica.
  
    * **Entrada:** Mira si estás en la lista de invitados. Si estás, pasas.
    * **Salida:** Cuando decides irte, el portero te ve y dice: *"Ah, yo te dejé entrar antes, puedes salir sin problemas"*. No vuelve a mirar ninguna lista.
      
* **Reglas:** Solo tiene reglas de "Permitir". Lo que no esté en la lista, está prohibido por defecto.

---

## 🚀 Ejemplo Práctico Paso a Paso: "Servir una Página Web"

Imagina que tienes un servidor web (Puerto 80) y quieres que un cliente vea tu web. Así viaja el dato:

### FASE 1: La Petición (Ida)

1.  **Internet ➔ ACL:** El cliente llega a la frontera. La ACL mira su regla de entrada: *"¿Se permite tráfico al puerto 80?"*. Si dice **SÍ**, el dato sigue.
2.  **ACL ➔ Grupo de Seguridad:** El dato llega a la puerta del servidor. El Grupo de Seguridad mira su lista: *"¿Está el puerto 80 permitido?"*. Si dice **SÍ**, el dato entra al servidor.
3.  **Servidor:** El servidor procesa la petición y prepara la página web para enviarla de vuelta.

### FASE 2: La Respuesta (Vuelta)

4.  **Servidor ➔ Grupo de Seguridad:** El dato sale del servidor. Como el Grupo de Seguridad es **Stateful**, recuerda que dejó entrar al cliente y **lo deja salir automáticamente**.
5.  **Grupo de Seguridad ➔ ACL:** El dato llega a la frontera para salir a Internet. **¡CUIDADO AQUÍ!** Como la ACL es **Stateless**, no recuerda al cliente. Debe existir una regla de salida específica (normalmente para los puertos efímeros) que diga: *"Se permite que el tráfico salga hacia Internet"*. Si no existe esa regla, el cliente nunca recibirá la web.

---

## 🛠️ Medidas de Seguridad y Buenas Prácticas

1.  **Principio de Menor Privilegio:** En los Grupos de Seguridad, abre solo los puertos estrictamente necesarios (ej. solo el 80 para web y el 22 para administración).
2.  **Defensa en Profundidad:** Usa ambos. El Grupo de Seguridad es tu primera línea de defensa para el servidor, y la ACL es tu red de seguridad para toda la subred.
3.  **Bloqueo de IPs Maliciosas (ACL):** Si detectas un ataque desde una IP específica, la **ACL** es el lugar ideal para ponerla en la "Lista Negra" (Deny), ya que el Grupo de Seguridad no permite reglas de denegación explícita.
4.  **Cierre por Defecto:** Recuerda que en AWS, si no creas una regla de permiso, el acceso está **denegado** automáticamente.

---

## 📊 Comparativa Final

| Característica | Grupo de Seguridad (Portero) | ACL de Red (Aduana) |
| :--- | :--- | :--- |
| **Nivel de protección** | Instancia (EC2) | Subred |
| **Estado (Memory)** | **Con estado (Stateful)** | **Sin estado (Stateless)** |
| **Reglas permitidas** | Solo permitir | Permitir y Denegar |
| **Orden de reglas** | Se evalúan todas | Se evalúan en orden numérico |
| **Aplicación** | Se aplica solo si se asigna | Se aplica a todos los recursos de la subred |

---

---
→ Volver al índice: [[📂Redes/00 - Índice Redes|🪐 Redes]]
